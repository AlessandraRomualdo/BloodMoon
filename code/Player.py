import pygame.key

from code.Const import (
    ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN,
    PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY,
    PLAYER_KEY_ALT_SHOOT
)
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.PlayerShotUp import PlayerShotUp


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # 🎥 Lista de imagens do personagem para animação
        self.frames = [
            pygame.image.load(f'./asset/{name}_0.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_1.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_2.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_3.png').convert_alpha()
        ]
        self.current_frame = 0
        self.animation_speed = 12  # Ajusta a velocidade da animação
        self.tick_count = 0

    def update(self):
        """Atualiza a animação do personagem"""
        self.tick_count += 1
        if self.tick_count >= self.animation_speed:
            self.tick_count = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]  # Troca o sprite

    def move(self):
        pressed_key = pygame.key.get_pressed()

        lower_limit = (WIN_HEIGHT / 2)

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > lower_limit:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()

            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

            if pressed_key[PLAYER_KEY_ALT_SHOOT[self.name]]:
                return PlayerShotUp(name=f'{self.name}ShotUp', position=(self.rect.centerx, self.rect.centery))
