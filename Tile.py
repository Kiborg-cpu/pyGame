import pygame
import config


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/wall.png').convert_alpha()
        self.id = 'tile'
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -14)