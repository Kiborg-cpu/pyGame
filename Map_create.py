import pygame

from Enemy import Enemy
from Ground import Ground
from Tile import Tile
from chest import Chest
from all_camera_sprites import all_camera_sprites
from config import tilemap, TILESIZE
from player import Player


class Map_create:
    def __init__(self):
        self.scaled = 1
        self.visible_sprites = all_camera_sprites()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(tilemap):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                Ground((x, y), [self.visible_sprites], self.scaled)
                if col == 'B':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'P':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                elif col == 'E':
                    Enemy((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'C':
                    Chest((x, y), [self.visible_sprites, self.obstacle_sprites])

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
