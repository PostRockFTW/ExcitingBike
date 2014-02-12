import sys
import pygame
import excitingbike.game.entities.track as track
from screen import Screen
from pygame.locals import *
from excitingbike.locals import *

class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()
        self.BGCOLOR = self.RED

        self.temporary_track_list = ["BLANK","BLANK","BLANK","A","G","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK"]

        self.loadLevel(self.temporary_track_list)

        self.currentOffset = 0
        self.bikerSpeed = 4

    def loadLevel(self, trackList):

        track_hurdles = [track.getTrackHurdle(hurdle) for hurdle in trackList]
        track_width = sum((surface.get_width() for surface in track_hurdles))
        track_height = track_hurdles[0].get_height()
        self.track_surface = pygame.Surface((track_width, track_height))

        # For now, just blit the hurdles to the level once
        xPos = 0
        for surface in track_hurdles:
            self.track_surface.blit(surface, (xPos, 0))
            xPos += surface.get_width()

    def update(self, events, states):

        self.currentOffset -= self.bikerSpeed

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

        self.displaysurf.blit(self.track_surface, (self.currentOffset, 0))
