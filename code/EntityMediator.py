from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:
    @staticmethod
    # this methos verifies if the images (sprites) are on the screen, if not, attrib zero to the heal so it can be destroyed
    def __verify_collision_window(ent: Entity):  # the __ indicates that this method only happens into this class
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for entity in entity_list:
            for i in range(len(entity_list)):
                test_list = entity_list[i]
                EntityMediator.__verify_collision_window(test_list)

    @staticmethod
    #this methos virifies if the health of an entity is lower than zero, if it's, removes it
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <=0:
                entity_list.remove(ent)

