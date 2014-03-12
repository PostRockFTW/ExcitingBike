import sys
import pygame
import game_screen
from menu_screen import MenuScreen
from option_menu_screen import OptionMenuScreen
from game_screen import GameScreen
from level_builder_screen import LevelBuilderScreen
from pygame.locals import *


class MainMenuScreen(MenuScreen):
    def __init__(self):

        super(MainMenuScreen,self).__init__()

        self.option_menu_instance = OptionMenuScreen()
        self.game_instance = GameScreen()
        self.level_builder_instance = LevelBuilderScreen()
        self.menu_options_dictionary = {"SINGLE PLAYER":self.game_instance, "MULTI PLAYER":self.game_instance, "LEVEL BUILDER": self.level_builder_instance, "OPTIONS":self.option_menu_instance}

        # set up Logo

        self.excitbike_logo = pygame.image.load("assets/excitebike_logo.png").convert()

        ### (width, height)
        self.EXCITBIKE_LOGO_SIZE = self.excitbike_logo.get_size()

        self.logo_location = [(self.WINDOWWIDTH-self.EXCITBIKE_LOGO_SIZE[0])/2,(self.WINDOWHEIGHT-self.EXCITBIKE_LOGO_SIZE[1])/4]

        # Menu logic variables
        self.myfont = pygame.font.Font("assets/Nintendo-NES-Font.ttf", 15)
        self.set_menu_options(("SINGLE PLAYER", "MULTI PLAYER", "LEVEL BUILDER", "OPTIONS"))

    def update(self,events,states):

            super(MainMenuScreen,self).update(events,states)
            # Logic Operations


            ### Logic for blinking selection

            self.blink_counter += 1
            if self.blink_counter > self.blink_speed:
                self.blink_state = not self.blink_state
                self.blink_counter = 0
            if self.blink_state:
                self.blink_color = self.WHITE
            else:
                self.blink_color = self.RED

            # fill the screen with stuff to be updated

            ### Background and logo

            self.displaysurf.fill(self.BGCOLOR)
            self.displaysurf.blit(self.excitbike_logo, self.logo_location)

            ### Menu Options

            for i in range(len(self.menu_options)):
                if i == self.menu_options_index:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.blink_color))
                else:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.WHITE))
                self.displaysurf.blit(self.fontsurface, (150, (275+i*25)))

            # Update Screen
