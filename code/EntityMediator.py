from oslo_config.types import Boolean

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    # this methos verifies if the images (sprites) are on the screen, if not, attrib zero to the heal so it can be destroyed
    def __verify_collision_window(ent: Entity):  # the __ indicates that this method only happens into this class
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):  # destroys the player shoot when it get outside window
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):  # destroys the enemy shoot when it get outside window
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    # this method verifies if the Enemies, Player and Shoots are colliding
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # this option have the same mean than valid_interaction == True
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod   # calculates the score while playing
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == "Player1Shot":
            for ent in entity_list:
                if ent.name == "Player1":
                    ent.score += enemy.score
        elif enemy.last_dmg == "Player2Shot":
            for ent in entity_list:
                if ent.name == "Player2":
                    ent.score += enemy.score


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # for entity in entity_list:
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(1 + i, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    # this methos virifies if the health of an entity is lower than zero, if it's, removes it
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
