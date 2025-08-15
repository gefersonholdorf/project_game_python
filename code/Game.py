import pygame
from code.Menu import Menu
from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True: 
            menu = Menu(self.window)
            menu_option_return = menu.run()
            
            if menu_option_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level01', menu_option_return)
                level_return = level.run()
            elif menu_option_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
            else:
                pass

