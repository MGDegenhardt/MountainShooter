#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]] :   # starts a new level for 1 player
                level = Level(self.window, "Level 1", menu_return)
                level_return = level.run()


            elif menu_return == MENU_OPTION[4]: # runs the close option
                pygame.quit()
                quit()
            else:
                pass




            # check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #        pygame.quit()  # closes the game window
            #       quit()  # end pygame



