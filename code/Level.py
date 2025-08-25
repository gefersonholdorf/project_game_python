from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame
from pygame import Surface, Rect
import pygame.font
from code.Const import WIN_WIDTH, COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, EVENT_BONUS, EVENT_TIMEOUT, COLOR_EMERALDA
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, menu_option_return):
        self.window = window
        self.name = name
        self.menu_option_return = menu_option_return
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('1'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 30000
        pygame.mixer.init()
        pygame.time.set_timer(EVENT_ENEMY, 2000)
        pygame.time.set_timer(EVENT_BONUS, 4000)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, ):
        clock = pygame.time.Clock()
        pygame.mixer.music.load('./asset/level.mp3')
        pygame.mixer.music.play(-1)
        while True:
            clock.tick(30)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if entity.name == 'Player':
                    self.level_text(24, f'Player - Score: {entity.health}', COLOR_EMERALDA, (110, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == EVENT_BONUS:
                    self.entity_list.append(EntityFactory.get_entity('Bonus'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout <= 0:
                        return self.menu_option_return

            self.level_text(24, f'{self.name} - Timeout: { self.timeout / 1000 :.1f}s', COLOR_WHITE, (120, 20))
            self.level_text(24, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (30, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)