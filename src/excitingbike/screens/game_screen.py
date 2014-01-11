import sys
import pygame
from screen import Screen
from ..game.entities.track import Track
from pygame.locals import *
from excitingbike.locals import *

class GameScreen(Screen):
    def __init__(self):
        super(GameScreen,self).__init__()
        self.biker1xlocation = 0
        self.biker1currentacceleration = 0
        self.BGCOLOR = self.RED

        self.current_track_list = ["START1","BLANK","BLANK","BLANK","A","G","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","END"]
        self.current_track = Track()
        self.current_track_surface = self.current_track.getThisTrack(self.current_track_list)

    ## TODO Update Biker Location Modules
    def place_holder_up(self):
        print "Up Button Pressed"

    def place_holder_down(self):
        print "Down Button Pressed"

    def place_holder_left(self):
        self.biker1xlocation += 10
        print "Left Button Pressed"

    def place_holder_right(self):
        self.biker1xlocation -= 10
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

        self.currentOffset = -self.biker1xlocation + (10*self.biker1currentacceleration)

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

        self.displaysurf.blit(self.current_track_surface, (self.currentOffset,0))
