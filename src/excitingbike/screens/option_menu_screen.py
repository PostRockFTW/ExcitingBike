import sys
import pygame
import game_screen
from menu_screen import MenuScreen
from pygame.locals import *

class OptionMenuScreen(MenuScreen):
    def __init__(self):

        super(OptionMenuScreen,self).__init__()

        self.set_menu_options(("INPUT OPTIONS", "AUDIO OPTIONS", "VIDEO OPTIONS"))
        self.menu_options_dictionary = {"SINGLE PLAYER":game_screen.GameScreen(), "MULTI PLAYER":game_screen.GameScreen(), "LEVEL BUILDER":game_screen.GameScreen()}

def update(self,events,states):

            super(MainMenuScreen,self).update(events,states)