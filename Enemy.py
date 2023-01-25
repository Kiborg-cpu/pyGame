import pygame
import random

from Draw_Text_on_Sprite import Draw_Text
from Sprite_sheet import Spritesheet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.groups = groups
        self.enemy_spritesheet = Spritesheet('assets/skeleton.png')
        self.animation_loop = 1
        self.id = 'enemy'
        self.player = None
        self.move_animations = [self.enemy_spritesheet.get_sprite(11, 37, 13, 27),
                                self.enemy_spritesheet.get_sprite(11, 69, 13, 27)]
        self.max_travel = random.randint(7, 50)
        self.image = self.enemy_spritesheet.get_sprite(11, 5, 9, 27)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(random.choice([-1, 1]), 0)
        self.hitbox = self.rect.inflate(0, -26)
        self.hitbox.size = (self.hitbox.height + 10, self.hitbox.width + 10)
        self.speed = 1
        self.hp = 200
        self.text_enemy = Draw_Text(groups[0], f'Skeleton: {self.hp}HP ', self)
        self.gambits = 0

    def update(self):
        self.move(self.speed)
        self.animate()
        if self.hp <= 0:
            self.kill()

    def setdamage(self, damage, player):
        self.hp -= damage
        self.text_enemy.update_text(f'Skeleton: {self.hp}HP', 'red')
        self.player = player
        self.move_towards_player(player)

    def move(self, speed):
        if self.player is None:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.hitbox.x -= self.direction.x * speed
            self.gambits += 1
            self.collision('horizontal')
            if self.gambits >= self.max_travel:
                self.direction.x *= -1
                self.gambits = 0
        else:
            self.move_towards_player(self.player)
        self.rect.center = self.hitbox.center

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        self.dirvect = pygame.math.Vector2(player.hitbox.x - self.hitbox.x,
                                      player.hitbox.y - self.hitbox.y)
        if self.dirvect.magnitude() != 0:
            self.dirvect.normalize()
            self.dirvect.scale_to_length(3)
        # Move along this normalized vector towards the player at current speed.
        self.hitbox.move_ip(self.dirvect)

    def animate(self):
        self.image = self.move_animations[int(self.animation_loop)]
        self.animation_loop += 0.2
        if self.animation_loop >= len(self.move_animations):
            self.animation_loop = 0

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.groups[1]:
                if sprite.id != 'enemy':
                    if sprite.rect.colliderect(self.hitbox):
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.hitbox.left = sprite.rect.right
                        self.direction.x *= -1

        if direction == 'vertical':
            for sprite in self.groups[1]:
                if sprite.id != 'enemy':
                    if sprite.rect.colliderect(self.hitbox):
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.rect.bottom
