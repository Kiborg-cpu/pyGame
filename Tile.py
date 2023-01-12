import pygame
import config


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, scaled):
        super().__init__(groups)
        self.image = pygame.image.load('assets/wall.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.image.get_size()[0]*scaled, self.image.get_size()[1]*scaled))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -2)
