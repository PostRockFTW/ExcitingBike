import sys
import pygame
from pygame.locals import *



class MenuScreen(object):
    def __init__(self):

        # set up a bunch of color tuples
        self.LIGHTBLUE = (100, 176, 255)
        self.DARKBLUE  = ( 20,  18, 167)
        self.WHITE     = (255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.RED       = (255,   0,   0)

        # Screen Settings
        self.SCREEN_MAGNIFIER = 2
        self.WINDOWWIDTH = 256*self.SCREEN_MAGNIFIER
        self.WINDOWHEIGHT = 224*self.SCREEN_MAGNIFIER
        self.WIN_CENTERX = int(self.WINDOWWIDTH / 2)
        self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2)

        self.DISPLAYSURF = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Exciting Bike')

        # set up Background

        self.BGCOLOR = self.DARKBLUE

        # Menu logic variables

        self.menu_options_index = 0
        self.menu_options = ["none"]
        self.selection = self.menu_options [self.menu_options_index]
        self.blink_speed = 8
        self.blink_counter = 0
        self.blink_state = True
        self.blink_color = self.RED

    def set_menu_options(self,arg):
        self.menu_options=arg
        self.update_selection()

    def update_selection(self):
        self.selection = self.menu_options [self.menu_options_index]

    def go_down(self):
        self.menu_options_index += 1
        if self.menu_options_index >= len(self.menu_options):
            self.menu_options_index = 0
        self.update_selection()

    def go_up(self):
        self.menu_options_index -= 1
        if self.menu_options_index < 0:
            self.menu_options_index += len(self.menu_options)
        self.update_selection()

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

            ### Menu Options

            self.myfont = pygame.font.Font("assets/Nintendo-NES-Font.ttf", 15)
            for i in range(len(self.menu_options)):
                if i == self.menu_options_index:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.blink_color))
                else:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.WHITE))
                self.DISPLAYSURF.blit(self.fontsurface, (150, (275+i*25)))

            # Update Screen
