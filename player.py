import math

import pygame
from pygame import KEYDOWN

import config
from Attack import Attack_sword
from Sprite_sheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, enemies_sprites, obstacle_sprites, scaled):
        super().__init__(groups)
        self.character_spritesheet = Spritesheet('assets/player.png')
        self.image = self.character_spritesheet.get_sprite(10, 2, 13, 28).convert_alpha()
        self.enemies_sprites = enemies_sprites
        self.is_anim = False
        #self.image = pygame.transform.smoothscale(self.image, (self.image.get_size()[0] * scaled, self.image.get_size()[1] * scaled)).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.HP = 20

        self.right_walk = [self.character_spritesheet.get_sprite(9, 34, 13, 28),
                           self.character_spritesheet.get_sprite(9, 66, 13, 28),
                           self.character_spritesheet.get_sprite(9, 2, 13, 28)]

        self.left_walk = [self.character_spritesheet.get_sprite(9, 130, 13, 28),
                          self.character_spritesheet.get_sprite(9, 162, 13, 28),
                          self.character_spritesheet.get_sprite(9, 98, 13, 28)]
        self.current_sprite = 0
        self.attack = Attack_sword()
        self.sprites_anim = []
        self.obstacle_sprites = obstacle_sprites

    def animate(self):
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites_anim):
            self.current_sprite = 0
        if len(self.sprites_anim) != 0:
            self.image = self.sprites_anim[int(self.current_sprite)]

    def input(self):
        keys = pygame.key.get_pressed()
        self.is_anim = True

        #if keys[pygame.K_SPACE]:
        #    self.attack.update(self)

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.sprites_anim = self.right_walk
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.sprites_anim = self.left_walk
        else:
            self.direction.x = 0
            self.current_sprite = 2
            self.is_anim = False

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        # self.rect.center += self.direction * speed

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def collision_enemy(self):
        for sprite in self.enemies_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.x > 0:
                    self.hitbox.right = sprite.hitbox.left
                if self.direction.x < 0:
                    self.hitbox.left = sprite.hitbox.right
                self.HP -= 10
                print(self.HP)
            if self.HP <= 0:
                self.kill()

    def update(self):
        self.input()
        self.move(self.speed)
        self.collision_enemy()
        self.animate()
