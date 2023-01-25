import pygame
from Sprite_sheet import Spritesheet


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.chest_spr = Spritesheet('assets/chest.png')
        self.anim_open = [self.chest_spr.get_sprite(8, 40, 17, 15).convert_alpha(),
                          self.chest_spr.get_sprite(8, 71, 17, 16).convert_alpha(),
                          self.chest_spr.get_sprite(8, 102, 17, 17).convert_alpha(),
                          self.chest_spr.get_sprite(6, 130, 19, 21).convert_alpha()]
        self.image = self.anim_open[0]
        self.id = 'chest'
        self.animation_loop = 0
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -14)
        self.isopen = True
        self.is_anim = True

    def open_chest(self):
        if self.is_anim:
            if not self.anim_open.index(self.image) == int(self.animation_loop):
                self.image = self.anim_open[int(self.animation_loop)]
                if int(self.animation_loop) >= 1:
                    self.rect.y = self.rect.y - (self.anim_open[int(self.animation_loop)].get_size()[1] - \
                                  self.anim_open[int(self.animation_loop) - 1].get_size()[1])
                    self.rect.x = self.rect.x - (self.anim_open[int(self.animation_loop)].get_size()[0] - \
                                                 self.anim_open[int(self.animation_loop) - 1].get_size()[0])
            self.animation_loop += 0.2
            if self.animation_loop >= len(self.anim_open):
                self.animation_loop = 0
                self.is_anim = False
                self.isopen = True

    def update(self):
        if not self.isopen:
            self.open_chest()
