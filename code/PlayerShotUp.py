from code.Const import ENTITY_SPEED
from code.PlayerShot import PlayerShot


class PlayerShotUp(PlayerShot):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]  # Move o tiro para cima
