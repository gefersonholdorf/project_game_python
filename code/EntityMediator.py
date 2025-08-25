from code.Entity import Entity
from code.Enemy import Enemy
from code.Bonus import Bonus
from code.Player import Player
from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH

class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right < 0:
                entity.health = 0
        if isinstance(entity, Bonus):
            if entity.rect.right < 0:
                entity.health = 0

    @staticmethod
    def __verify_collision_entity(entity1, entity2):
        is_valid_collision = False
        if isinstance(entity1, Player) and isinstance(entity2, Bonus):
            is_valid_collision = True
        elif isinstance(entity1, Bonus) and isinstance(entity2, Player):
            is_valid_collision = True
        elif isinstance(entity1, Player) and isinstance(entity2, Enemy):
            is_valid_collision = True
        elif isinstance(entity1, Enemy) and isinstance(entity2, Player):
            is_valid_collision = True

        if is_valid_collision:
            if (entity1.rect.right >= entity2.rect.left and entity1.rect.left <= entity2.rect.right and entity1.rect.bottom >= entity2.rect.top and entity1.rect.top <= entity2.rect.bottom):
                entity1.health -= entity2.damage
                entity2.health -= entity1.damage
                entity1.last_dmg = entity2.name
                entity2.last_dmg = entity1.name


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)
                

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)