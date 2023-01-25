from Map_create import Map_create
from UI import UI
from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Dungeon_survive')
        self.clock = pygame.time.Clock()
        # pygame.event.set_grab(True)
        self.font = pygame.font.Font('assets/shrift.ttf', 32)
        self.level = Map_create()
        self.ui = UI()

    # def game_over(self):
    #    text = self.font.render('Game over', True, WHITE)
    #    text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
    #    restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)
    #
    #    for sprite in self.all_camera_sprites:
    #        sprite.kill()
    #
    #    while self.running:
    #        for event in pygame.event.get():
    #            if event.type == pygame.QUIT:
    #                self.running = False
    #        mouse_pos = pygame.mouse.get_pos()
    #        mouse_pressed = pygame.mouse.get_pressed()
    #
    #        if restart_button.is_pressed(mouse_pos, mouse_pressed):
    #            self.new()
    #            self.main()
    #        self.screen.blit(self.intro_background, (0, 0))
    #        self.screen.blit(text, text_rect)
    #        self.screen.blit(restart_button.image, restart_button.rect)
    #        self.clock.tick(FPS)
    #        pygame.display.update()
    #
    # def intro_screen(self):
    #    intro = True
    #    # title = self.font.render('Game', True, WHITE)
    #    # title_rect = title.get_rect(x=60, y=80)
    #    play_button = Button(40, 120, 100, 50, WHITE, BLACK, 'Play', 32)
    #    while intro:
    #        for event in pygame.event.get():
    #            if event.type == pygame.QUIT:
    #                intro = False
    #                self.running = False
    #
    #        mouse_pos = pygame.mouse.get_pos()
    #        mouse_pressed = pygame.mouse.get_pressed()
    #
    #        if play_button.is_pressed(mouse_pos, mouse_pressed):
    #            intro = False
    #
    #        self.screen.blit(self.intro_background, (0, 0))
    #        # self.screen.blit(title, title_rect)
    #        self.screen.blit(play_button.image, play_button.rect)
    #        self.clock.tick(FPS)
    #        pygame.display.update()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEWHEEL:
                    self.level.visible_sprites.zoom_scale += event.y * 0.03
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            self.ui.show_health(self.level.player.HP / self.level.player.health_ratio,
                                self.level.player.health_bar_length, self.level.player.HP)
            if self.level.player.attack is not None:
                self.ui.debug(self.level.visible_sprites.zoom_scale, self.level.player.attack.rect.x)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
