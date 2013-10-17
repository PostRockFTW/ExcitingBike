import sys
import pygame

from pygame.locals import *

# Screen Settings

SCREEN_MAGNIFIER = 2
WINDOWWIDTH = 256*SCREEN_MAGNIFIER
WINDOWHEIGHT = 224*SCREEN_MAGNIFIER
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 60

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Exciting Bike')

# set up a bunch of image constants 
LIGHTBLUE = (100, 176, 255)
DARKBLUE  = ( 20,  18, 167)
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)

BGCOLOR = DARKBLUE

excitbike_logo = pygame.image.load("../../assets/excitebike_logo.png").convert()
# (width, height)
EXCITBIKE_LOGO_SIZE = excitbike_logo.get_size()

logo_location = [(WINDOWWIDTH-EXCITBIKE_LOGO_SIZE[0])/2,(WINDOWHEIGHT-EXCITBIKE_LOGO_SIZE[1])/2
                 ]

# Menu logic variables

menu_options = ("Single Player", "Multi Player", "Level Builder")
menu_options_index = 0
selection = menu_options [menu_options_index]
fontcount = 0
pygame.init()
pygame.font.init()
fonts = pygame.font.get_fonts()
clock = pygame.time.Clock()
print len(fonts)
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            menu_options_index += 1
            if menu_options_index > len(menu_options):
                menu_options_index -= len(menu_options)
        elif event.type == KEYDOWN and event.key == K_UP:
            menu_options_index -= 1
            if menu_options_index < 0:
                menu_options_index += len(menu_options)
                
    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(excitbike_logo, logo_location)
    fontcount += 1
    if fontcount >= len(fonts):
        fontcount -= len(fonts)
    myfont = pygame.font.SysFont(fonts[fontcount], 15)
    label = myfont.render("Some text!", 1, (255,255,0))
    DISPLAYSURF.blit(label, (100, (fontcount*15)))
    pygame.display.update()
    print (fontcount)                
    clock.tick(30)
