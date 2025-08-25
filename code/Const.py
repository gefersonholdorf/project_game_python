import pygame

WIN_WIDTH = 960
WIN_HEIGHT = 540

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255) 

MENU_OPTION = ('Novo Jogo',
'Sair')

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    '1': 10,
    '2': 10,
    '3': 10,
    '4': 10,
    '5': 10,
    '6': 10,
    'Player': 10,
    'Enemy': 5
}