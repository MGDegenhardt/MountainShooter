#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self ):
        pass
