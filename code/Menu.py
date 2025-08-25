import pygame
from pygame import Surface, Rect
import pygame.font
from code.Const import WIN_WIDTH, COLOR_WHITE, COLOR_ORANGE, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        pygame.mixer.init()
        self.surf = pygame.image.load('./asset/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Corre CLT", COLOR_WHITE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 200 + 40 * i)) 
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 40 * i)) 

            # Check for all events
            for event in pygame.event.get(): 
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()
                if (event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_DOWN):
                        if (menu_option < len(MENU_OPTION) -1):
                            menu_option += 1
                        else:
                            menu_option = 0
                    if(event.key == pygame.K_UP):
                        if (menu_option > 0):
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if(event.key == pygame.K_RETURN):
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)