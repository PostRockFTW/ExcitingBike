import sys
import pygame
from pygame.locals import *



class MenuScreen(object):
    def __init__(self):

        # Screen Settings
        self.SCREEN_MAGNIFIER = 2
        self.WINDOWWIDTH = 256*self.SCREEN_MAGNIFIER
        self.WINDOWHEIGHT = 224*self.SCREEN_MAGNIFIER
        self.WIN_CENTERX = int(self.WINDOWWIDTH / 2)
        self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2)

        self.FPS = 60

        self.DISPLAYSURF = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Exciting Bike')

        # set up a bunch of color tuples
        self.LIGHTBLUE = (100, 176, 255)
        self.DARKBLUE  = ( 20,  18, 167)
        self.WHITE     = (255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.RED       = (255,   0,   0)

        # set up Background and Logo

        self.BGCOLOR = self.DARKBLUE

        self.excitbike_logo = pygame.image.load("assets/excitebike_logo.png").convert()

        ### (width, height)
        self.EXCITBIKE_LOGO_SIZE = self.excitbike_logo.get_size()

        self.logo_location = [(self.WINDOWWIDTH-self.EXCITBIKE_LOGO_SIZE[0])/2,(self.WINDOWHEIGHT-self.EXCITBIKE_LOGO_SIZE[1])/4]

        # Menu logic variables

        self.menu_options = ["SINGLE PLAYER", "MULTI PLAYER", "LEVEL BUILDER"]
        self.menu_options_index = 0
        self.selection = self.menu_options [self.menu_options_index]
        self.blink_speed = 8
        self.blink_counter = 0
        self.blink_state = True
        self.blink_color = self.RED

        pygame.init()

        pygame.font.init()

    def go_down(self):
        self.menu_options_index += 1
        if self.menu_options_index >= len(self.menu_options):
            self.menu_options_index = 0

    def go_up(self):
        self.menu_options_index -= 1
        if self.menu_options_index < 0:
            self.menu_options_index += len(self.menu_options)

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
