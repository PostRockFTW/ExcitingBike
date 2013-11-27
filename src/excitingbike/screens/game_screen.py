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
        self.displaysurf = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))

    def update(self,events,states):
        self.displaysurf.fill((255,   0,   0))