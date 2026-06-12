#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # game mode: 1 ou  2 players
        self.entity_list: list[Entity]=[]

    def run(self, ):
        pass
