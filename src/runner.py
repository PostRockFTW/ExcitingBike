import sys
import pygame
from excitingbike.screens.menu_screen import MenuScreen
from excitingbike.screens.main_menu_screen import MainMenuScreen
from excitingbike.screens.option_menu_screen import OptionMenuScreen
from excitingbike.screens.game_screen import GameScreen
from excitingbike.controller.controller import Controller

from pygame.locals import *
from excitingbike.locals import *

# Runs the main loop of the program
class Runner(object):

    def __init__(self, initial_screen):

        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = initial_screen
        self.screen_resolution = 2
        self.WINDOWWIDTH = 256*self.screen_resolution
        self.WINDOWHEIGHT = 224*self.screen_resolution
        self.main_display = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.key.set_repeat(50, 50)

        # Load Game State Instances

        self.controller_instance = Controller()
        self.main_menu_instance = MainMenuScreen()
        self.states = [self.main_menu_instance]

    def run(self):

        # Variable initial states
        running = True

        while running:

            # Beginning Phase

            for event in pygame.event.get(pygame.QUIT):
                if event.type == pygame.QUIT:
                    running = False

            # Draw Step
            current_inputs = self.controller_instance.process_events()

            # Main Phase
            for event in current_inputs:
                if event == KEY_ESCAPE:
                    self.states.pop()

            if len(self.states) <= 0:
                running = False
                continue

            # Combat Phase
            self.states[-1].update(current_inputs,self.states)

            # Post Combat Phase
            self.main_display.blit(self.states[-1].displaysurf, (0,0))
            pygame.display.update()

            pygame.display.set_caption('Exciting Bike (FPS: %0.2f)' % self.clock.get_fps())

            # End Step
            self.clock.tick(30)

        pygame.quit()
        sys.exit()
