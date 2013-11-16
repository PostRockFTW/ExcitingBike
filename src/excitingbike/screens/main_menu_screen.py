import sys
import pygame
import game_screen
from menu_screen import MenuScreen
from pygame.locals import *


class MainMenuScreen(MenuScreen):
    def __init__(self):

        super(MainMenuScreen,self).__init__()

        # set up Logo

        self.excitbike_logo = pygame.image.load("assets/excitebike_logo.png").convert()

        ### (width, height)
        self.EXCITBIKE_LOGO_SIZE = self.excitbike_logo.get_size()

        self.logo_location = [(self.WINDOWWIDTH-self.EXCITBIKE_LOGO_SIZE[0])/2,(self.WINDOWHEIGHT-self.EXCITBIKE_LOGO_SIZE[1])/4]

        # Menu logic variables

        self.set_menu_options(("SINGLE PLAYER", "MULTI PLAYER", "LEVEL BUILDER", "OPTIONS"))

    def update(self):
            # Logic Operations


            ### Logic for blinking selection

            self.blink_counter += 1
            if self.blink_counter > self.blink_speed:
                self.blink_state = not self.blink_state
                self.blink_counter = 0
            if self.blink_state == True:
                self.blink_color = self.WHITE
            else:
                self.blink_color = self.RED

            # fill the screen with stuff to be updated

            ### Background and logo

            self.DISPLAYSURF.fill(self.BGCOLOR)
            self.DISPLAYSURF.blit(self.excitbike_logo, self.logo_location)

            ### Menu Options

            self.myfont = pygame.font.Font("assets/Nintendo-NES-Font.ttf", 15)
            for i in range(len(self.menu_options)):
                if i == self.menu_options_index:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.blink_color))
                else:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.WHITE))
                self.DISPLAYSURF.blit(self.fontsurface, (150, (275+i*25)))

            # Update Screen
