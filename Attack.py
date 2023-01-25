import pygame

from Sprite_sheet import Spritesheet


class Attack_sword(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)
        self.player = player
        self.id = 'attack'
        self.damage = 2
        self.attack_sprite_r = Spritesheet('assets/sword_right.png')
        self.attack_sprite_l = Spritesheet('assets/sword_left.png')
        self.sword_anim_right = [  # self.attack_sprite_r.get_sprite(11, 9, 4, 23).convert_alpha(),
            self.attack_sprite_r.get_sprite(41, 24, 23, 4).convert_alpha(),
            self.attack_sprite_r.get_sprite(41, 24, 23, 4).convert_alpha()]
        self.sword_anim_left = [  # self.attack_sprite_l.get_sprite(16, 9, 4, 23).convert_alpha(),
            self.attack_sprite_l.get_sprite(32, 24, 23, 4).convert_alpha(),
            self.attack_sprite_l.get_sprite(32, 24, 23, 4).convert_alpha()]
        self.enemy = groups[0]
        self.sword_anim = self.sword_anim_right
        if self.player.direction.x == 1 or self.player.old_dir.x == 1:
            self.sword_anim = self.sword_anim_right
            self.old_dir = 1
        elif self.player.direction.x == -1 or self.player.old_dir.x == -1:
            self.sword_anim = self.sword_anim_left
        self.image = self.sword_anim[0].convert_alpha()
        self.rect = self.image.get_rect()
        self.animation_loop = 0
        self.is_start = False
        # self.hitbox = self.rect.inflate(0, -17)

    def update(self):
        self.animate()

        if self.is_start:
            # self.rect = self.image.get_rect()
            if self.player.direction.x == 1 or self.player.old_dir.x == 1:
                self.sword_anim = self.sword_anim_right
                self.old_dir = 1
                if self.animation_loop >= 1:
                    self.rect.topleft = self.player.rect.midright
                else:
                    self.rect.topleft = self.player.rect.midleft
            elif self.player.direction.x == -1 or self.player.old_dir.x == -1:
                self.sword_anim = self.sword_anim_left
                self.old_dir = -1
                if self.animation_loop >= 1:
                    self.rect.topright = self.player.rect.midleft
                else:
                    self.rect.topright = self.player.rect.midright
            self.collide()
        else:

            if self.player.direction.x == 1 or self.player.old_dir.x == 1:
                self.sword_anim = self.sword_anim_right
                self.old_dir = 1
                self.rect.topleft = self.player.rect.midleft
            elif self.player.direction.x == -1 or self.player.old_dir.x == -1:
                self.sword_anim = self.sword_anim_left
                self.old_dir = -1
                self.rect.topright = self.player.rect.midright

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.enemy, False)
        for hit in hits:
            if hit.id == 'enemy':
                hit.setdamage(self.damage, self.player)
                if self.player.old_dir[0] > 0:
                    hit.hitbox.x += 10
                if self.player.old_dir[0] < 0:
                    hit.hitbox.x -= 10
                self.player.sprite_text.update_text('attack', 'red')

    def animate(self):
        self.image = self.sword_anim[int(self.animation_loop)]
        self.animation_loop += 0.1
        if self.animation_loop >= len(self.sword_anim_left):
            self.animation_loop = 0
            self.is_start = False
