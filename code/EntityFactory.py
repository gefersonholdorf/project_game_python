from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Enemy import Enemy
import random

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case '1':
                list_bg = []

                for i in range(6):
                    list_bg.append(Background(str(i + 1), (0, 0)))
                    list_bg.append(Background(str(i + 1), (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (20, 400))
            case 'Enemy':
                return Enemy('Enemy', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
