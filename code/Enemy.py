from code.Entity import Entity
import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.score = 0
        self.lives = 3
    
    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

