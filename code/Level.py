import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import  WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAW_TIME, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, C_RED_DARK, C_RED_DARKEST
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = (EntityFactory.get_entity('Player1'))
        player.score = player_score[0]
        self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(120)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()

                    if shoot is not None:
                        self.entity_list.append(shoot)
                 # mostrar na tela o health e score dos players
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} - SCORE: {ent.score}', C_RED_DARKEST, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # adicionando os inimigos na tela
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    # condição para passar de fase timeout
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score

                        return True
                    # condição de fim de jogo player morrer
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # print texto
            self.level_text(24, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_RED_DARK, (10, 5))
            self.level_text(24, f'fps: {clock.get_fps():.0f}', C_RED_DARK, (10, WIN_HEIGHT - 35))
            pygame.display.flip()
            # invocar o mediador
            EntityMediator.verify_collision(entity_list=self.entity_list)
            # verifica a vida e destroi a entidade
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)