#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from abc import ABC, abstractmethod
from code.Background import Background

class EntityFactory(ABC):

    @staticmethod
    def create_entities(entity_name: str, position=(0, 0)):
        match entity_name:  # verifies whitch level is selected
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0,0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Player1":
                return Player(f"Player1", (20,WIN_HEIGHT/2 - 30))
            case "Player2":
                return Player(f"Player2", (20, WIN_HEIGHT / 2 + 30))
