import pygame

# W
WIN_WIDTH=900
WIN_HEIGHT=506

#C
C_RED_DARK=(186, 0, 0)
C_RED_DARKEST=(107, 0, 0)

# E
ENTITY_SPEED={
'Level1Bg0': 0,
'Level1Bg1': 1,
'Level1Bg2': 2,
'Level1Bg3': 3,
'Level1Bg4': 3,
'Level1Bg5': 3,
'Level1Bg6': 3,
'Level2Bg0': 0,
'Level2Bg1': 1,
'Level2Bg2': 2,
'Level2Bg3': 3,
'Level2Bg4': 3,
'Level2Bg5': 3,
'Level2Bg6': 3,
'Player1': 3,
'Player1Shot': 1,
'Player1ShotUp': 1,
'Enemy1': 1,
'Enemy1Shot': 5,
'Enemy2': 1,
'Enemy2Shot': 2,
'Enemy3': 1,
'Enemy3Shot': 2,
}

ENTITY_SCORE={
'Level1Bg0': 0,
'Level1Bg1': 0,
'Level1Bg2': 0,
'Level1Bg3': 0,
'Level1Bg4': 0,
'Level1Bg5': 0,
'Level1Bg6': 0,
'Level2Bg0': 0,
'Level2Bg1': 0,
'Level2Bg2': 0,
'Level2Bg3': 0,
'Level2Bg4': 0,
'Level2Bg5': 4,
'Level2Bg6': 4,
'Player1': 0,
'Player1Shot': 0,
'Player1ShotUp': 0,
'Enemy1': 100,
'Enemy1Shot': 0,
'Enemy2': 125,
'Enemy2Shot': 0,
'Enemy3': 125,
'Enemy3Shot': 0,
}

EVENT_ENEMY=pygame.USEREVENT + 1
EVENT_TIMEOUT=pygame.USEREVENT + 2

ENTITY_HEALTH={
'Level1Bg0': 999,
'Level1Bg1': 999,
'Level1Bg2': 999,
'Level1Bg3': 999,
'Level1Bg4': 999,
'Level1Bg5': 999,
'Level1Bg6': 999,
'Level2Bg0': 999,
'Level2Bg1': 999,
'Level2Bg2': 999,
'Level2Bg3': 999,
'Level2Bg4': 999,
'Level2Bg5': 4,
'Level2Bg6': 4,
'Player1': 200,
'Player1Shot': 1,
'Player1ShotUp': 1,
'Enemy1': 50,
'Enemy1Shot': 1,
'Enemy2': 60,
'Enemy2Shot': 1,
'Enemy3': 70,
'Enemy3Shot': 1,
}

ENTITY_SHOT_DELAY={
'Player1': 20,
'Enemy1': 100,
'Enemy2': 200,
'Enemy3': 200
}

ENTITY_DAMAGE={
'Level1Bg0': 0,
'Level1Bg1': 0,
'Level1Bg2': 0,
'Level1Bg3': 0,
'Level1Bg4': 0,
'Level1Bg5': 0,
'Level1Bg6': 0,
'Level2Bg0': 0,
'Level2Bg1': 0,
'Level2Bg2': 0,
'Level2Bg3': 0,
'Level2Bg4': 0,
'Level2Bg5': 4,
'Level2Bg6': 4,
'Player1': 1,
'Player1Shot': 25,
'Player1ShotUp': 20,
'Enemy1': 1,
'Enemy1Shot': 20,
'Enemy2': 1,
'Enemy2Shot': 15,
'Enemy3': 1,
'Enemy3Shot': 15,
}

#M
MENU_OPTION=('NEW GAME 1P',
             'SCORE',
             'EXIT'
             )

# P
PLAYER_KEY_UP={'Player1': pygame.K_UP}
PLAYER_KEY_DOWN={'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT={'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT={'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT={'Player1': pygame.K_RCTRL}
PLAYER_KEY_ALT_SHOOT = {'Player1': pygame.K_RSHIFT}

#S

SPAW_TIME=3000
SCORE_POS={
'Title': (WIN_WIDTH / 2, 50),
'EnterName': (WIN_WIDTH / 2, 80),
'Label': (WIN_WIDTH / 2, 120),
'Name': (WIN_WIDTH / 2, 130),
0: (WIN_WIDTH / 2, 140),
1: (WIN_WIDTH / 2, 150),
2: (WIN_WIDTH / 2, 160),
3: (WIN_WIDTH / 2, 170),
4: (WIN_WIDTH / 2, 180),
}

#T
TIMEOUT_STEP=100
TIMEOUT_LEVEL=40000