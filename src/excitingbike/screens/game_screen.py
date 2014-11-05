import pygame

from ..game.gfx import track as Track
from ..game.gfx.biker import Biker
from screen import Screen
from ..locals import *


class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()
        self.BGCOLOR = self.RED

        self.temporary_track_list = ["BLANK","BLANK","BLANK","A","G","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK"]

        self.start_hurdles = [Track.getTrackHurdle(hurdle) for hurdle in ("START1", "START2", "START3")]
        self.start_hurdle_width = self.start_hurdles[0].get_width()

        self.track_surface = self.loadLevel(self.temporary_track_list)
        self.background_surface =  pygame.image.load("assets/Excitebike_BackGround.png").convert()

        self.heatBarWidth       = 31.0
        self.heatBarHeight      = 8.0
        self.heatBarBorderWith  = 1
        self.heat               = 0

        self.biker = Biker()

        self.resetGame()

        self.friction       = 0.1
        self.acceleration_a = .2
        self.acceleration_b = 1

        self.bikerSpeed    = 0
        self.maxBikerSpeed = 4

        self.currentOffset = 0

        self.lane       = 2
        self.targetLane = 2

        self.minrange   = 1
        self.maxrange   = 4
        self.lanerange  = (self.minrange, self.maxrange)

        #Event handling lists
        self.eventStates = []
        self.lastEventStates = []

    def loadLevel(self, trackList):

        self.track_hurdles = [Track.getTrackHurdle(hurdle) for hurdle in trackList]
        self.track_width = sum((surface.get_width() for surface in self.track_hurdles))
        self.track_height = self.track_hurdles[0].get_height()
        self.track_surface = pygame.Surface((self.track_width, self.track_height))

        # For now, just blit the hurdles to the level once
        xPos = self.start_hurdle_width
        for surface in self.track_hurdles:
            self.track_surface.blit(surface, (xPos, 0))
            xPos += surface.get_width()

        return self.track_surface

    def resetGame(self):
        self.started = False
        self.started_time = 0

    def update(self, events, states):

        #pygame.draw.rect(self.displaysurf,
        #                     pygame.Color("black"),
        #                     pygame.Rect(0,
        #                                 0,
        #                                 self.WINDOWWIDTH,
        #                                 self.WINDOWHEIGHT))
        self.displaysurf.blit(self.background_surface, (0,0))
        self.displaysurf.blit(self.track_surface, (self.currentOffset, 72))

        self.displaysurf.blit(self.start_hurdles[-1], (self.currentOffset, 72))

        if not self.started:
            if self.started_time == 0:
                self.started_time = pygame.time.get_ticks()
            else:
                curTime = pygame.time.get_ticks()
                msPassed = curTime - self.started_time

                # TODO: make this agnostic as to the # of start hurdles
                if 0 <= msPassed < 1000:
                    self.displaysurf.blit(self.start_hurdles[0], (0, 0))
                elif 1000 <= msPassed < 2000:
                    self.displaysurf.blit(self.start_hurdles[1], (0, 0))
                elif msPassed > 3000:
                    self.started = True

        else: # Game is active
            self.currentOffset -= self.bikerSpeed

        self.bikerSpeed -= self.friction

        # Handle inputs

        # Create/Wipe Event States
        self.eventStates = [False for i in range(9)]#number of input types ##Todo make this reflexive to max(events)

        #Populate Event States
        for i in events: #Event Types are stored as numbers starting at 0
            self.eventStates[i] = True
            # FROM LOCALS
            #KEY_UP       = 0
            #KEY_DOWN     = 1
            #KEY_LEFT     = 2
            #KEY_RIGHT    = 3
            #KEY_A_BUTTON = 4
            #KEY_B_BUTTON = 5
            #KEY_START    = 6
            #KEY_SELECT   = 7
            #KEY_ESCAPE   = 8
        if self.eventStates[0]    == True:
            if self.lastEventStates[0] == False:
                self.targetLane = self.targetLane - 1
                pass
        if self.eventStates[1]    == True:
            if self.lastEventStates[1] == False:
                self.targetLane = self.targetLane + 1
                pass
        if self.eventStates[4]    == True:
            # 1.5 seconds to get to full speed
            self.bikerSpeed += self.acceleration_a
            pass
        if self.eventStates[5]    == True:
            self.bikerSpeed += self.acceleration_b
            pass
        if self.eventStates[2]    == True:
            #Todo change to biker angle
            self.biker.left()
        if self.eventStates[3]    == True:
            self.biker.right()
        if self.eventStates[6]    == True:
            if self.heat > 0:
                self.heat -= 1
                pass
        if self.eventStates[7]    == True:
            if self.heat < self.heatBarWidth:
                self.heat += 1
                pass
        if self.eventStates[8]    == True:
            self.place_holder_escape()

        pass
        self.lastEventStates = self.eventStates



        # Restrict to lanes between minrange and maxrange
        self.targetLane = max(self.lanerange[0],
                              min(self.lanerange[-1], self.targetLane))

        self.bikerSpeed = max(0,
                              min(self.bikerSpeed, self.maxBikerSpeed))

        direction = -1 if self.lane > self.targetLane else 1

        # This executes for some reason??
        # if self.lane != self.targetLane:

        if abs(self.lane - self.targetLane) > 0.01:
            self.lane += direction * 0.2

        # Update graphics
        self.displaysurf.blit(self.biker.displaysurf,
                              (0,
                               self.yPosForLane(self.lane)))


        heatBarRect = pygame.Rect(144 - self.heatBarWidth,
                                  209 - self.heatBarHeight,
                                  self.heatBarWidth,
                                  self.heatBarHeight)
        # Heat bar border
        #pygame.draw.rect(self.displaysurf,
         #                pygame.Color("red"),
          #               heatBarRect,
           #              self.heatBarBorderWith)

        heatBarRect.width *= self.heat / self.heatBarWidth
        # Heat bar
        pygame.draw.rect(self.displaysurf,
                         pygame.Color("red"),
                         heatBarRect)


    def yPosForLane(self, lane):
        laneHeight = 12
        verticalOffset = 90
        return (lane * laneHeight) + verticalOffset

