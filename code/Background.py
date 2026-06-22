#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]    # moves the background items in accord it's speed
        if self.rect.right <= 0:        # when the right side of the picture reaches the zero
            self.rect.left = WIN_WIDTH  # sets the left side to the end of the screen




