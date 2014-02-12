import sys
import pygame
import excitingbike.game.entities.track as track
from screen import Screen
from pygame.locals import *
from excitingbike.locals import *

class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()
        self.biker1xlocation = 0
        self.biker1currentacceleration = 0
        self.BGCOLOR = self.RED

        self.current_track_list = ["BLANK","BLANK","BLANK","A","G","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK"]
        self.current_track_surface = track.getThisTrack(self.current_track_list)

        self.bikerSpeed = 4

    def loadLevel(self, trackList):

        self.track_surface_array = [self.getTrackHurdle(hurdle_surface) for hurdle_surface in track_list]
        self.track_width = sum((surface.get_width() for surface in self.track_surface_array))
        self.track_surface = pygame.Surface((self.track_width,self.TRACK_HEIGHT))
        self.width_counter = 0
        for surface in self.track_surface_array:
            self.track_surface.blit(surface, (self.width_counter,0))
            self.width_counter += surface.get_width ()
        return self.track_surface
        pass

    def update(self, events, states):

        self.currentOffset = -self.biker1xlocation + (10*self.biker1currentacceleration)

        # Event Operations

        for event in events:
            """
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
            """
            pass

        # fill the screen with stuff to be updated

        ### Place Holder Background

        self.displaysurf.blit(self.current_track_surface, (self.currentOffset,0))
