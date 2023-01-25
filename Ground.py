import pygame
import config
from Sprite_sheet import Spritesheet


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, groups, scaled):
        super().__init__(groups)
        self.spr = Spritesheet('assets/ground.png')
        self.image = self.spr.get_sprite(0, 0, 32, 32).convert_alpha()
        self.id = 'ground'
        self.image = pygame.transform.smoothscale(self.image, (
        self.image.get_size()[0] * scaled, self.image.get_size()[1] * scaled))
        self.rect = self.image.get_rect(topleft=pos)
