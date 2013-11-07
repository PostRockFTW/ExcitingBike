import sys
import pygame
import excitingbike.screens.menu_screen
from pygame.locals import *

# Runs the main loop of the program
class Runner(object):

    def __init__(self, initial_screen):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = initial_screen
        self.main_display = pygame.display.set_mode((800, 600))
        self.initial_menu = excitingbike.screens.menu_screen.MenuScreen()

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
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    self.initial_menu.go_down()
                elif event.type == KEYDOWN and event.key == K_UP:
                    self.initial_menu.go_up()
            # Draw Phase
            ##inputs.update

            # Main Phase
            if current_state == "menu":
                self.initial_menu.update()
                #menu_selection = menu_screen.getselection()
                #if menu_selection <> None:
                #    current_state = menu_selection


            elif current_state == "game":
                print "current state is game"

            # Combat Phase
            self.main_display.blit(self.initial_menu.DISPLAYSURF, (0,0))
            pygame.display.update()
            # TODO: Blit to main display
            # self.main_display.update()

            # End Step
            self.clock.tick(30)

        pygame.quit()
        sys.exit()
