import random

import pygame
import config
from Sprite_sheet import Spritesheet


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.spr = Spritesheet('assets/ground.png')
        self.arr_images_floor = [self.spr.get_sprite(0, 0, 32, 32).convert_alpha(),
                                 self.spr.get_sprite(0, 96, 32, 32).convert_alpha()]
                                 #self.spr.get_sprite(0, 128, 32, 32).convert_alpha()]
                                 #self.spr.get_sprite(0, 160, 32, 32).convert_alpha()]
        self.image = random.choice(self.arr_images_floor)
        self.id = 'ground'
        self.rect = self.image.get_rect(topleft=pos)
