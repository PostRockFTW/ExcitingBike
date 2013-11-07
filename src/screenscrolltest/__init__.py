import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()

    gameWidth = 460
    gameHeight = 230
    miniMapFactor = 8

    mainSurface = pygame.display.set_mode((gameWidth, gameHeight))
    mainClock = pygame.time.Clock()
    FPS = 30

    pygame.display.set_caption('Screen Scroll Test')

    print "Move screen with left/right arrow keys"
    print "Hold SHIFT to jump to edges"

    backgroundSurface = pygame.image.load('background.png').convert()
    miniMapSurface = pygame.Surface((backgroundSurface.get_width()/miniMapFactor, backgroundSurface.get_height()/miniMapFactor))
    pygame.transform.scale(backgroundSurface, (miniMapSurface.get_width(), miniMapSurface.get_height()), miniMapSurface)

    running = True
    currOffset = 0

    # Game loop
    while running:
        pygame.event.pump()
        for event in pygame.event.get():
            if ((event.type == QUIT) or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                running = False

        # Draw the current section of the background
        mainSurface.blit(backgroundSurface, (-currOffset, 0))

        miniMapLeft = mainSurface.get_width() - miniMapSurface.get_width()

        mainSurface.blit(miniMapSurface, (miniMapLeft, 0))

        miniMapBorderRect = pygame.Rect(
            miniMapLeft + currOffset * (float(miniMapSurface.get_width()) / backgroundSurface.get_width()),
            0,
            miniMapSurface.get_width() * (float(mainSurface.get_width()) / backgroundSurface.get_width()),
            miniMapSurface.get_height()
        )

        pygame.draw.rect(mainSurface, pygame.color.Color('white'), miniMapBorderRect, 2)

        pressedKeys = pygame.key.get_pressed()
        shiftPressed = pressedKeys[K_LSHIFT] or pressedKeys[K_RSHIFT]
        if (pressedKeys[K_RIGHT]):
            currOffset += 10
            rightMost = (backgroundSurface.get_width() - mainSurface.get_width())
            if (currOffset > rightMost) or shiftPressed:
                currOffset = rightMost
        elif (pressedKeys[K_LEFT]):
            currOffset -= 10
            if (currOffset < 0) or shiftPressed:
                currOffset = 0


        pygame.display.update()

        mainClock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
