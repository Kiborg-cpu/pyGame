import pygame
import random

from Draw_Text_on_Sprite import Draw_Text
from Sprite_sheet import Spritesheet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites
        self.enemy_spritesheet = Spritesheet('assets/skeleton.png')
        self.animation_loop = 1
        self.id = 'enemy'
        self.old_dir = pygame.math.Vector2(0, 0)
        self.player = None
        self.collision_arr = [False] * 9
        self.direction_text = ''
        self.move_animations = [self.enemy_spritesheet.get_sprite(11, 37, 13, 27),
                                self.enemy_spritesheet.get_sprite(11, 69, 13, 27)]
        self.max_travel = random.randint(7, 50)
        self.image = self.enemy_spritesheet.get_sprite(11, 5, 9, 27)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(random.choice([-1, 1]), 0)
        self.hitbox = self.rect.inflate(0, -19)
        self.speed = 1
        self.hp = 200
        self.sprite_text = Draw_Text(groups[0], f'Skeleton: {self.hp}HP ', self)
        self.gambits = 0

    def update(self):
        self.move(self.speed)
        self.animate()
        if self.hp <= 0:
            self.sprite_text.remove_text()
            self.kill()

    def setdamage(self, damage, player):
        self.hp -= damage
        self.sprite_text.update_text(f'Skeleton: {self.hp}HP', 'red')
        self.player = player
        self.move_towards_player(player)

    def move(self, speed):
        if self.player is None:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.hitbox.x -= self.direction.x * speed
            self.gambits += 1
            if self.gambits >= self.max_travel:
                self.direction.x *= -1
                # self.image = self.move_animations[]
                self.old_dir = self.direction
                self.gambits = 0
        else:
            self.move_towards_player(self.player)
            self.collision()
        self.rect.center = self.hitbox.center

    def move_towards_player(self, player):
        self.dirvect = pygame.math.Vector2(player.hitbox.centerx - self.hitbox.centerx,
                                           player.hitbox.centery - self.hitbox.centery)
        if self.dirvect.magnitude() != 0:
            self.dirvect.normalize()
            self.dirvect.scale_to_length(3)
        self.hitbox.move_ip(self.dirvect)

    def collision(self):
        if self.player.hitbox.colliderect(self.hitbox):
            self.player.set_damage(1)
            self.collide_nine_points(self.player.hitbox)
            self.find_collision_direction_by_points()
            if 'left' in self.direction_text:
                self.player.otbras.x = -2
            if 'right' in self.direction_text:
                self.player.otbras.x = 2
            if 'top' in self.direction_text:
                self.player.otbras.y = -2
            if 'bottom' in self.direction_text:
                self.player.otbras.y = 2
            self.player.start_ticks = pygame.time.get_ticks()

    def collide_nine_points(self, rect):
        self.collision_arr[0] = rect.collidepoint(self.rect.topleft)
        self.collision_arr[1] = rect.collidepoint(self.rect.topright)
        self.collision_arr[2] = rect.collidepoint(self.rect.bottomleft)
        self.collision_arr[3] = rect.collidepoint(self.rect.bottomright)

        self.collision_arr[4] = rect.collidepoint(self.rect.midleft)
        self.collision_arr[5] = rect.collidepoint(self.rect.midright)
        self.collision_arr[6] = rect.collidepoint(self.rect.midtop)
        self.collision_arr[7] = rect.collidepoint(self.rect.midbottom)

        self.collision_arr[8] = rect.collidepoint(self.rect.center)

    def find_collision_direction_by_points(self):
        self.direction_text = ''
        if self.collision_arr[0] or self.collision_arr[2] or self.collision_arr[4]:
            self.direction_text += "left "

        elif self.collision_arr[1] or self.collision_arr[3] or self.collision_arr[5]:
            self.direction_text += "right "

        if self.collision_arr[0] or self.collision_arr[1] or self.collision_arr[6]:
            self.direction_text += "top "

        elif self.collision_arr[2] or self.collision_arr[3] or self.collision_arr[7]:
            self.direction_text += "bottom "

        # if self.collision_arr[8]:
        #    self.direction_text += "center "

        print(self.direction_text)

    def animate(self):
        self.image = self.move_animations[int(self.animation_loop)]
        self.animation_loop += 0.2
        if self.animation_loop >= len(self.move_animations):
            self.animation_loop = 0
