import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level3', menu_return, player_score)
                    level_return = level.run(player_score)
                    # se terminar o level 2 salva o score
                    if level_return:
                        score.save_score(menu_return, player_score)
            elif menu_return == MENU_OPTION[1]:
                score.show_score()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit() # fechar a janela
                quit()  # finaliza pygame
            else:
                pass
