#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self ):
        speed = ENTITY_SPEED[self.name]
        self.rect.centerx -= speed  # moves the ENEMY towards the left
