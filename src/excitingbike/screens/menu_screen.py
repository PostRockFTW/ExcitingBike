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

# set up a bunch of color tuples

LIGHTBLUE = (100, 176, 255)
DARKBLUE  = ( 20,  18, 167)
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)

# set up Background and Logo

BGCOLOR = DARKBLUE

excitbike_logo = pygame.image.load("../../assets/excitebike_logo.png").convert()

### (width, height)
EXCITBIKE_LOGO_SIZE = excitbike_logo.get_size()

logo_location = [(WINDOWWIDTH-EXCITBIKE_LOGO_SIZE[0])/2,(WINDOWHEIGHT-EXCITBIKE_LOGO_SIZE[1])/4
                 ]

# Menu logic variables

menu_options = ["SINGLE PLAYER", "MULTI PLAYER", "LEVEL BUILDER"]
menu_options_index = 0
selection = menu_options [menu_options_index]
blink_speed = 8
blink_counter = 0
blink_state = True
blink_color = RED

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()

while True:
    # event handling loop for quit events / Inputs
    ### to be replaced/modified later with a call to another class
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYUP and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_DOWN:
            menu_options_index += 1
            if menu_options_index >= len(menu_options):
                menu_options_index = 0
        elif event.type == KEYDOWN and event.key == K_UP:
            menu_options_index -= 1
            if menu_options_index < 0:
                menu_options_index += len(menu_options)

    # Logic Operations


    ### Logic for blinking selection

    blink_counter += 1
    if blink_counter > blink_speed:
        blink_state = not blink_state
        blink_counter = 0
    if blink_state == True:
        blink_color = WHITE
    else:
        blink_color = RED

    # fill the screen with stuff to be updated

    ### Background and logo

    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(excitbike_logo, logo_location)

    ### Menu Options

    myfont = pygame.font.Font("../../assets/Nintendo-NES-Font.ttf", 15)
    for i in range(len(menu_options)):
        if i == menu_options_index:
            fontsurface = (myfont.render(menu_options[i], 1, blink_color))
        else:
            fontsurface = (myfont.render(menu_options[i], 1, WHITE))
        DISPLAYSURF.blit(fontsurface, (150, (275+i*25)))

    # Update Screen

    pygame.display.update()

    clock.tick(30)