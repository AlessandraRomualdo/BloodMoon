
import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import  SCORE_POS, MENU_OPTION, C_RED_DARKEST
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')
        name = ''
        score = ''
        while True:
            self.score_text(48, 'YOU WIN!!', C_RED_DARKEST, SCORE_POS['Title'])
            text = ''
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player enter your name (4 characters):'

            self.score_text(20, text, C_RED_DARKEST, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score })
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_RED_DARKEST, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 5', C_RED_DARKEST, SCORE_POS['Title'])
        self.score_text(20, '       NAME       SCORE       ', C_RED_DARKEST, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top5()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score = player_score
            self.score_text(20, f'{name}        -    {score}', C_RED_DARKEST,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Comic Sans MS", text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

