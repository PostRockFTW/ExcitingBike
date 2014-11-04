import sys

import pygame

from excitingbike.screens.main_menu_screen import MainMenuScreen
from excitingbike.controller.controller import Controller
from excitingbike.locals import *


# Runs the main loop of the program
class Runner(object):

    def __init__(self, initial_screen):


        self.clock = pygame.time.Clock()
        self.screen = initial_screen
        self.screen_resolution = 2
        self.WINDOWWIDTH = 256*self.screen_resolution
        self.WINDOWHEIGHT = 224*self.screen_resolution
        self.main_display = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))

        # Load Game State Instances

        self.controller_instance = Controller()
        self.main_menu_instance = MainMenuScreen()
        self.states = [self.main_menu_instance]

    def run(self):

        # Variable initial states
        running = True

        while running:

            # Beginning Phase

            # Draw Step
            events = self.controller_instance.process_events()

            # Main Phase
            for event in events:
                if event == EVENT_QUIT:
                    running = False
                    continue
                elif event == KEY_ESCAPE:
                    self.states.pop()

            if len(self.states) <= 0:
                running = False
                continue

            # Combat Phase
            self.states[-1].update(events, self.states)

            # Post Combat Phase
            self.main_display.blit(self.states[-1].displaysurf, (0,0))
            pygame.display.update()

            pygame.display.set_caption('Exciting Bike (FPS: %0.2f)' % self.clock.get_fps())

            # End Step
            delatTime = self.clock.tick(30)

        pygame.quit()
        sys.exit()
