import sys
import pygame
from pygame.locals import *

# Runs the main loop of the program
class Runner(object):

    def __init__(self, initial_screen):

        pygame.init()

        self.screen = initial_screen
        self.main_display = pygame.display.set_mode((800, 600))

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if ((event.type == QUIT) or
                    (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False

            self.screen.update()
            # TODO: Blit to main display
            # self.main_display.update()

        pygame.quit()
        sys.exit()
