import random

import pygame


class Draw_Text(pygame.sprite.Sprite):
    def __init__(self, groups, text, player):
        super().__init__(groups)
        self.text = text
        self.player = player
        self.id = 'text'
        self.color = 'white'
        self.font = pygame.font.Font('assets/shrift.ttf', 18)
        self.image = self.font.render(self.text, True, self.color)
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2))
        self.rect = self.image.get_rect(bottomleft=(self.player.rect.topleft[0], self.player.rect.topleft[1] - 5))
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        if self.color == 'white':
            self.rect.bottomleft = self.player.rect.topleft
        elif self.color == 'red':
            self.rect.bottomleft = self.player.rect.topleft
            self.rect.x -= random.randrange(0, 5)
            self.rect.y -= random.randrange(0, 5)
        elif self.color == 'yellow':
            self.rect.y -= 5
            self.image = pygame.transform.scale(self.image,
                                                (self.image.get_size()[0] + 1, self.image.get_size()[1] + 1))
        else:
            self.rect.y -= 5
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000  # calculate how many seconds
        print(seconds)
        if seconds >= 3:
            self.image.fill((0, 0, 0, 0))

    def update_text(self, text, color):
        self.color = color
        self.text = text
        self.font = pygame.font.Font('assets/shrift.ttf', 18)
        self.image = self.font.render(self.text, True, self.color)
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2))
        self.rect = self.image.get_rect(bottomleft=(self.player.rect.topleft[0] - random.randrange(0, 10), self.player.rect.topleft[1] - random.randrange(0, 10)))
        self.start_ticks = pygame.time.get_ticks()
