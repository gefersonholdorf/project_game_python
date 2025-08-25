import pygame

WIN_WIDTH = 960
WIN_HEIGHT = 540

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255) 
COLOR_EMERALDA = (80, 200, 120)

MENU_OPTION = ('Novo Jogo',
'Sair')

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_BONUS = pygame.USEREVENT + 2
EVENT_TIMEOUT = pygame.USEREVENT + 3

ENTITY_SPEED = {
    '1': 10,
    '2': 10,
    '3': 10,
    '4': 10,
    '5': 10,
    '6': 10,
    'Player': 10,
    'Enemy': 5,
    'Bonus': 12
}

ENTITY_HEALTH = {
    '1': 999,
    '2': 999,
    '3': 999,
    '4': 999,
    '5': 999,
    '6': 999,
    'Player': 2000,
    'Enemy': 50,
    'Bonus': 50
}

ENTITY_DAMAGE = {
    '1': 999,
    '2': 999,
    '3': 999,
    '4': 999,
    '5': 999,
    '6': 999,
    'Player': 50,
    'Enemy': 300,
    'Bonus': -200
}