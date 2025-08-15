from code.Background import Background
from code.Const import WIN_WIDTH

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
