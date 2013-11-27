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

        # Load Game State Instances

        self.controller_Instance = Controller()

        self.main_Menu_Instance = MainMenuScreen()
        self.option_Menu_Instance = OptionMenuScreen()
        self.game_Instance = GameScreen()
        self.current_state = self.main_Menu_Instance
        self.menu_options_dictionary = {"SINGLE PLAYER":self.game_Instance, "MULTI PLAYER":self.game_Instance, "LEVEL BUILDER":self.game_Instance, "OPTIONS":self.option_Menu_Instance}

    def run(self):

        # Variable initial states
        running = True

        while running:

            # Upkeep
            current_inputs = self.controller_Instance.process_events()

            # Draw Phase
            for event in current_inputs:
                if event == KEY_ESCAPE:
                    running = False
                elif event == KEY_DOWN:
                    self.current_state.go_down()
                elif event == KEY_UP:
                    self.current_state.go_up()
                elif event == KEY_A_BUTTON:
                    print self.current_state
                    self.current_state = self.menu_options_dictionary[self.current_state.selection]



            # Main Phase
            self.current_state.update()

            # Combat Phase
            self.main_display.blit(self.current_state.DISPLAYSURF, (0,0))
            pygame.display.update()
            # TODO: Blit to main display
            # self.main_display.update()

            # End Step
            self.clock.tick(30)

        pygame.quit()
        sys.exit()
