import pygame
import random

from Sprite_sheet import Spritesheet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.enemy_spritesheet = Spritesheet('assets/skeleton.png')
        self.animation_loop = 1
        self.move_animations = [self.enemy_spritesheet.get_sprite(11, 37, 13, 27),
                                self.enemy_spritesheet.get_sprite(11, 69, 13, 27)]
        self.max_travel = random.randint(7, 50)
        self.image = self.enemy_spritesheet.get_sprite(11, 5, 9, 27)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(random.choice([-1, 1]), 0)
        self.hitbox = self.rect.inflate(0, -26)
        self.speed = 1
        self.gambits = 0

    def update(self):
        self.move(self.speed)
        self.animate()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x -= self.direction.x * speed
        self.gambits += 1
        if self.gambits >= self.max_travel:
            self.direction.x *= -1
            self.gambits = 0
        self.rect.center = self.hitbox.center

    def animate(self):
        self.image = self.move_animations[int(self.animation_loop)]
        self.animation_loop += 0.2
        if self.animation_loop >= len(self.move_animations):
            self.animation_loop = 0
