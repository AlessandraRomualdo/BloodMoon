import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # Lista de imagens do personagem para animação
        self.frames = [
            pygame.image.load(f'./asset/{name}_0.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_1.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_2.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_3.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_4.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_5.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_6.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_7.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_8.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_9.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_10.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_11.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_12.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_13.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_14.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_15.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_16.png').convert_alpha(),
            pygame.image.load(f'./asset/{name}_17.png').convert_alpha(),
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
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))