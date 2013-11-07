import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()

    mainSurface = pygame.display.set_mode((460, 230))
    mainClock = pygame.time.Clock()
    FPS = 30

    backgroundSurface = pygame.image.load('background.png').convert()

    running = True
    currOffset = 0

    # Game loop
    while running:
        pygame.event.pump()
        for event in pygame.event.get():
            if ((event.type == QUIT) or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                running = False

        mainSurface.blit(backgroundSurface, (-currOffset, 0))

        currOffset = (currOffset + 5) % (backgroundSurface.get_width() - mainSurface.get_width())

        pygame.display.update()

        mainClock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
