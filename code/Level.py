#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Player import Player
from code.EntityFactory import EntityFactory
from code.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # game mode: 1 ou  2 players
        self.entity_list: list[Entity]=[]
        self.entity_list.extend(EntityFactory.create_entities("Level1Bg"))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest= ent.rect)
            pygame.display.flip()

        pass
