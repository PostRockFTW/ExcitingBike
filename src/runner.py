import sys
import pygame
from pygame.locals import *

# Runs the main loop of the program
class Runner(object):

    def __init__(self, initial_screen):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = initial_screen
        self.main_display = pygame.display.set_mode((800, 600))

    def run(self):
        # Variable initial states
        current_state = "menu"
        running = True

        while running:

            # Upkeep
            for event in pygame.event.get():
                if ((event.type == QUIT) or
                    (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False

            # Draw Phase
            ##inputs.update

            # Main Phase
            if current_state == "menu":
                menu_screen.give_inputs
                menu_screen.update
                menu_selection = menu_screen.getselection()
                if menu_selection <> None:
                    current_state = menu_selection
                print "current state is menu"

            elif current_state == "game":
                print "current state is game"

            # Combat Phase
            self.screen.update()
            # TODO: Blit to main display
            # self.main_display.update()

            # End Step
            self.clock.tick

        pygame.quit()
        sys.exit()
