import pygame

from Sprite_sheet import Spritesheet


class Raztyazka(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.groups = groups
        self.id = 'plita'
        self.boom_anim = [Spritesheet('assets/explosion0.png').get_sprite_chose_color_key(0, 0, 80, 125, 'white').convert_alpha(),
                          Spritesheet('assets/explosion1.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion2.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion3.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion4.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion5.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion6.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion7.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha(),
                          Spritesheet('assets/explosion8.png').get_sprite_chose_color_key(0, 0, 80, 125,'white').convert_alpha()]

        self.image = Spritesheet('assets/raztyazka.png').get_sprite(0, 0, 32, 32)
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_loop = 0
        self.is_anim = False
        self.player = None
        self.hitbox = self.rect.inflate(0, -14)

    def active_lovuchka(self):
        for sprite in self.groups[0]:
            if sprite.rect.colliderect(self.hitbox):
                if sprite.id == 'player':
                    self.player = sprite
                    self.is_anim = True
                    sprite.kill()

    def animate(self):
        if self.is_anim:
            self.image = self.boom_anim[int(self.animation_loop)]
            self.rect.center = self.player.rect.topleft
            self.animation_loop += 0.2
            if self.animation_loop >= len(self.boom_anim):
                self.animation_loop = 0
                self.is_anim = False

    def update(self):
        self.active_lovuchka()
        self.animate()
