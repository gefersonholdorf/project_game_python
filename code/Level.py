from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame

class Level:
    def __init__(self, window, name, menu_option_return):
        self.window = window
        self.name = name
        self.menu_option_return = menu_option_return
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('1'))

    def run(self, ):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
        pass