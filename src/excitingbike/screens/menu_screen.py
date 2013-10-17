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

menu_options = ("SINGLE PLAYER", "MULTI PLAYER", "LEVEL BUILDER")
menu_options_index = 0
selection = menu_options [menu_options_index]


pygame.init()

pygame.font.init()
fonts = pygame.font.get_fonts()
fontcount = len(fonts)

clock = pygame.time.Clock()

print fontcount

while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            menu_options_index += 1
            #Use this after font is picked
            #if menu_options_index > len(menu_options):
            #    menu_options_index -= len(menu_options)
        elif event.type == KEYDOWN and event.key == K_UP:
            menu_options_index -= 1
            #Use this after font is picked
            #if menu_options_index < 0:
            #    menu_options_index += len(menu_options)
                
    # fill the screen with stuff to be updated
    
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(excitbike_logo, logo_location)
    myfont = pygame.font.Font("../../assets/Nintendo-NES-Font.ttf", 15)
    for i in range(len(menu_options)):
            fontsurface = (myfont.render(menu_options[i], 1, (255,255,0)))
            DISPLAYSURF.blit(fontsurface, (100, (350+i*25)))

    # fill the screen to draw from a blank state
    pygame.display.update()
    print (fontcount)                
    clock.tick(30)
