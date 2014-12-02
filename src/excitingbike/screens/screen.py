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
        self.screen_resolution = 2
        self.WINDOWWIDTH = 256
        self.WINDOWHEIGHT = 224
        self.setWidth(self.WINDOWWIDTH)
        self.setHeight(self.WINDOWHEIGHT)

        self.initDisplaySurf()

        # set up Background

        self.BGCOLOR = self.DARKBLUE


    def setWidth(self, width):
        self.WINDOWWIDTH = self.screen_resolution * width
        self.WIN_CENTERX = int(self.WINDOWWIDTH / 2)

        self.initDisplaySurf()

    def setHeight(self, height):
        self.WINDOWHEIGHT = self.screen_resolution * height
        self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2)

        self.initDisplaySurf()

    def initDisplaySurf(self):
        self.displaysurf = pygame.surface.Surface((self.WINDOWWIDTH, self.WINDOWHEIGHT))
