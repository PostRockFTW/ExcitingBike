import sys
import pygame
from screen import Screen
from pygame.locals import *
from excitingbike.locals import *

class GameScreen(Screen):
    def __init__(self):

        super(GameScreen,self).__init__()

        self.BGCOLOR = self.RED

    # Abilities all games should have

    ## TODO Update Biker Location Modules
    def place_holder_up(self):
        print "Up Button Pressed"

    def place_holder_down(self):
        print "Down Button Pressed"

    def place_holder_left(self):
        print "Left Button Pressed"

    def place_holder_right(self):
        print "Right Button Pressed"

    def place_holder_a(self):
        print "A Button Pressed"

    def place_holder_b(self):
        print "B Button Pressed"

    def place_holder_start(self):
        print "Start Button Pressed"

    def place_holder_select(self):
        print "Select Button Pressed"

    def update(self,events,states):

        # Event Operations

        for event in events:
            if event == KEY_DOWN:
                self.place_holder_down()
            elif event == KEY_UP:
                self.place_holder_up()
            elif event == KEY_LEFT:
                self.place_holder_left()
            elif event == KEY_RIGHT:
                self.place_holder_right()
            elif event == KEY_A_BUTTON:
                self.place_holder_a()
            elif event == KEY_B_BUTTON:
                self.place_holder_b()
            elif event == KEY_START:
                self.place_holder_start()
            elif event == KEY_SELECT:
                self.place_holder_select()

        # fill the screen with stuff to be updated

        ### Place Holder Background

        self.displaysurf.fill(self.BGCOLOR)
