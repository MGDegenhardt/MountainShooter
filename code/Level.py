#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.examples.grid import WINDOW_WIDTH
from pygame.font import Font

from code.Const import COL_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COL_GREEN, COL_CYAN
from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.EntityFactory import EntityFactory
from code.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # establishes the game duration up to 20 seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode  # game mode: 1 ou  2 players
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.create_entities("Level1Bg"))  # creates the entities for the background
        self.entity_list.append(EntityFactory.create_entities("Player1"))  # creates the player entity

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.create_entities("Player2"))  # creates the second player entity

        # at every nth seconds an enemy should be spawn
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, ):
        pygame.mixer_music.load("./assets/" + "Level1" + ".mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.Shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == "Player1":
                        self.level_text(14, f"Player 1 - Health: {ent.health} | Score: {ent.score}", COL_GREEN, (10, 25))
                    if ent.name == "Player2":
                        self.level_text(14, f"Player 2 - Health: {ent.health} | Score: {ent.score}", COL_CYAN, (10, 45))

            for event in pygame.event.get():  # this event verifies if the app should close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.create_entities(choice))

            # printing game information on the screen
            self.level_text(14, f"{self.name} + Timeout:{self.timeout / 1000 : .1f}s", COL_WHITE, (10, 5))
            self.level_text(14, f"fps: {clock.get_fps() : .0f}", COL_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f"entidades: {len(self.entity_list)}", COL_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()
            # here the collisions and live are tested
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(text_surf, text_rect)

        # pass
