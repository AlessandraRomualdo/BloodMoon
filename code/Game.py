import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        menu = Menu(self.window)
        menu_return = menu.run()

        if menu_return in [MENU_OPTION[0]]:
            player_score = [0, 0]
            level = Level(self.window, 'Level1', menu_return, player_score)
            level_return = level.run()
        elif menu_return == MENU_OPTION[2]:
            pygame.quit()  # fechar a janela
            quit()  # finaliza pygame
        else:
            pass

