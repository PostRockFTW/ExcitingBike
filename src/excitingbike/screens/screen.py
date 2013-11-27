import sys
import pygame

from pygame.locals import *
from excitingbike.locals import *

class Screen(object):
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

        self.displaysurf = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Exciting Bike')

        # set up Background

        self.BGCOLOR = self.DARKBLUE