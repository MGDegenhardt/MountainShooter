#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./assets/" + name + ".png").convert_alpha() # creates a generic image
        self.rect = self.surf.get_rect(left = position[0], top = position[1]) # creates yhe rectangle were the image will be displayed
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, 1)
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = "None"

    @abstractmethod
    def move(self, ):
        pass
