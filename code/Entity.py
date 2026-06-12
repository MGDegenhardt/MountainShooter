#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./assets/" + name + ".png") # creates a generic image
        self.rect = self.surf.get_rect(left = position[0], top = position[1]) # creates yhe rectangle were the image will be displayed
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
