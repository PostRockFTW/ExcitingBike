import sys
import pygame
from pygame.locals import *
class GameScreen:
    def __init__(self):
        self.SCREEN_MAGNIFIER = 2
        self.WINDOWWIDTH = 256*self.SCREEN_MAGNIFIER
        self.WINDOWHEIGHT = 224*self.SCREEN_MAGNIFIER
        self.WIN_CENTERX = int(self.WINDOWWIDTH / 2)
        self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2)
        self.DISPLAYSURF = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        print("placeholder") # TODO remove this line & implement

    def update(self):
        print("Updating game screen")
        self.DISPLAYSURF.fill((255,   0,   0))