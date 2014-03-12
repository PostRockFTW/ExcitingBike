import pygame.surface

class Screen(object):
    def __init__(self):

        # set up a bunch of color tuples
        self.LIGHTBLUE = (100, 176, 255)
        self.DARKBLUE  = ( 20,  18, 167)
        self.WHITE     = (255, 255, 255)
        self.BLACK     = (  0,   0,   0)
        self.RED       = (255,   0,   0)

        # Screen Settings
        self.myfont = pygame.font.Font("assets/Nintendo-NES-Font.ttf", 15)
        self.SCREEN_MAGNIFIER = 2
        width = 256
        height = 224

        self.WINDOWWIDTH = width
        self.WINDOWHEIGHT = height
        self.setWidth(width)
        self.setHeight(height)

        self.initDisplaySurf()

        # set up Background

        self.BGCOLOR = self.DARKBLUE


    def setWidth(self, width):
        self.WINDOWWIDTH = self.SCREEN_MAGNIFIER * width
        self.WIN_CENTERX = int(self.WINDOWWIDTH / 2)

        self.initDisplaySurf()

    def setHeight(self, height):
        self.WINDOWHEIGHT = self.SCREEN_MAGNIFIER * height
        self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2)

        self.initDisplaySurf()

    def initDisplaySurf(self):
        self.displaysurf = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
