#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from abc import ABC, abstractmethod
from code.Background import Background

class EntityFactory(ABC):

    @staticmethod
    def create_entities(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0,0)))
                return list_bg
