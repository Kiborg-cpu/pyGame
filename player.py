import pygame

from Attack import Attack_sword
from Draw_Text_on_Sprite import Draw_Text
from Sprite_sheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.font = pygame.font.Font('assets/shrift.ttf', -10)
        self.vis_sp = groups[0]
        self.character_spritesheet = Spritesheet('assets/player.png')
        self.image = self.character_spritesheet.get_sprite(10, 2, 13, 28).convert_alpha()
        self.is_anim = False
        self.id = 'player'
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -15)
        self.old_dir = pygame.math.Vector2(1, 0)
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.HP = 20
        self.otbras = pygame.math.Vector2(0, 0)
        self.maximum_health = 20
        self.health_bar_length = 20
        self.health_ratio = self.maximum_health / self.health_bar_length

        self.right_walk = [self.character_spritesheet.get_sprite(9, 34, 13, 28),
                           self.character_spritesheet.get_sprite(9, 66, 13, 28),
                           self.character_spritesheet.get_sprite(9, 2, 13, 28)]

        self.left_walk = [self.character_spritesheet.get_sprite(9, 130, 13, 28),
                          self.character_spritesheet.get_sprite(9, 162, 13, 28),
                          self.character_spritesheet.get_sprite(9, 98, 13, 28)]
        self.current_sprite = 0
        self.sprites_anim = []
        self.obstacle_sprites = obstacle_sprites
        self.sprite_text = Draw_Text(groups, 'I am alive', self)
        self.attack = Attack_sword(groups, self)
        self.start_ticks = 0

    def animate(self):
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites_anim):
            self.current_sprite = 0
        if len(self.sprites_anim) != 0:
            self.image = self.sprites_anim[int(self.current_sprite)]

    def input(self):
        keys = pygame.key.get_pressed()
        self.is_anim = True

        if keys[pygame.K_SPACE]:
            self.attack.is_start = True

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_e]:
            for sprite in list(filter(lambda sprite: sprite.id == 'chest', self.obstacle_sprites)):
                if sprite.rect.colliderect(self.hitbox):
                    sprite.isopen = False
                    self.sprite_text.update_text('stonks+++++++++++++++', 'yellow')

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
        if self.direction.x != 0:
            self.old_dir = self.direction

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.otbras == (0, 0):
            self.hitbox.x += self.direction.x * speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * speed
            self.collision('vertical')
            self.rect.center = self.hitbox.center
        else:
            self.hitbox.x += self.otbras.x * speed
            self.collision_otbras('horizontal')
            self.hitbox.y += self.otbras.y * speed
            self.collision_otbras('vertical')
            self.rect.center = self.hitbox.center
        # self.rect.center += self.direction * speed

    def set_damage(self, damage):
        self.HP -= damage

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

    def collision_otbras(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.otbras.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.otbras.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.otbras.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.otbras.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
        self.animate()
        if self.otbras.x != 0 or self.otbras.y != 0:
            if (pygame.time.get_ticks() - self.start_ticks) / 1000 >= 0.2:
                self.otbras.x = 0
                self.otbras.y = 0
