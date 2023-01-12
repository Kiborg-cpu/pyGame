import pygame
from Sprite_sheet import Spritesheet


class Attack_sword(pygame.sprite.Sprite):
    def __init__(self):
        self.attack_sprite = Spritesheet('assets/sword.png')
        self.sword_anim = [self.attack_sprite.get_sprite(11, 9, 4, 23),
                           self.attack_sprite.get_sprite(41, 9, 32, 32),
                           self.attack_sprite.get_sprite(41, 9, 32, 32)]
        self.animation_loop = 0

    def update(self, player):
        #self.rect.x = player.rect.x + 20
        #self.rect.y = player.rect.y
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        self.image = self.sword_anim[int(self.animation_loop)]
        self.animation_loop += 0.2
        if self.animation_loop >= len(self.sword_anim):
            self.kill()
