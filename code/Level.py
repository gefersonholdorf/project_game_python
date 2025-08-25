from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame
from pygame import Surface, Rect
import pygame.font
from code.Const import WIN_WIDTH, COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY

class Level:
    def __init__(self, window, name, menu_option_return):
        self.window = window
        self.name = name
        self.menu_option_return = menu_option_return
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('1'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self, ):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

            self.level_text(18, f'{self.name} - Timeout: { self.timeout / 1000 :.1f}s', COLOR_WHITE, (90, 20))
            self.level_text(18, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (30, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)