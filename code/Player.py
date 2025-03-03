import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, PLAYER_KEY_ALT_SHOOT
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.PlayerShotUp import PlayerShotUp


class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        

    def update(self):
        pass

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Definir o limite inferior como a metade da altura da tela
        lower_limit = WIN_HEIGHT / 2

        # Mover para cima, mas sem ultrapassar a metade inferior da tela
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > lower_limit:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Mover para baixo, sem ultrapassar a borda inferior da tela
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Mover para esquerda eixo x
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Mover para direita eixo x
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()

            # Tiro normal (vai para frente)
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

            # Tiro alternativo (vai para cima)
            if pressed_key[PLAYER_KEY_ALT_SHOOT[self.name]]:
                return PlayerShotUp(name=f'{self.name}ShotUp', position=(self.rect.centerx, self.rect.centery))
