import pygame


class UI:
    def __init__(self):
        self.dis = pygame.display.get_surface()
        self.font = pygame.font.Font('assets/shrift.ttf', 20)
        self.health_bar_len = 60
        self.max_hp = 20

    def show_health(self, health_ratio, health_bar_length, curr_hp):
        pygame.draw.rect(self.dis, 'White', (10, 18, curr_hp*5, 25), 4)
        pygame.draw.rect(self.dis, 'Red', (10, 18, health_ratio*5, 25))
        img = self.font.render(str(curr_hp), True, 'White')
        self.dis.blit(img, (18, 21))

    def debug(self, zoomsc, attack, fps):
        img = self.font.render('zoom: '+str(zoomsc), True, 'White')
        #attack_pl = self.font.render('att_coord: ' + str(attack), True, 'White')
        fps = self.font.render('FPS: ' + str(fps), True, 'White')
        self.dis.blit(fps, (400, 21))

