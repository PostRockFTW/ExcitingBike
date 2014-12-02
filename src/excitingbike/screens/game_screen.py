import pygame

from ..game.gfx import track as Track
from ..game.gfx.biker import Biker
from ..game.gfx.track import Track
from screen import Screen
from ..locals import *
from ..input.input import Input


class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()

        # Set up instances for gamescreen objects

        #State Surface???
        self.background_surface =  pygame.image.load("assets/Excitebike_BackGround.png").convert()

        #Track
        self.track = Track()

        #Biker
        self.biker_1 = Biker()

        #Heat Bar
        self.heatBarWidth       = 31.0
        self.heatBarHeight      = 8.0
        self.heatBarBorderWith  = 1
        self.heat               = 0

        #Intro Animation
        self.start_hurdles = [self.track.getTrackHurdle(hurdle) for hurdle in ("START1",
                                                                               "START2",
                                                                               "START3")]
        self.start_hurdle_width = self.start_hurdles[0].get_width()
        self.resetGame()

    def resetGame(self):
        self.started = False
        self.started_time = 0

    def update(self, events, states):
        #Update Background gfx to wipe screen

        self.displaysurf.blit(self.background_surface, (0,0))
        self.displaysurf.blit(self.track.track_sprite,
                             (self.track.current_displaysurf_x_position,
                              self.track.displaysurf_y_position))
        self.displaysurf.blit(self.start_hurdles[-1],
                             (self.track.current_displaysurf_x_position,
                              self.track.displaysurf_y_position))

        #Game start animation logic todo move game start animation to separate class
        if not self.started:
            if self.started_time == 0:
                self.started_time = pygame.time.get_ticks()
            else:
                curTime = pygame.time.get_ticks()
                msPassed = curTime - self.started_time

                # TODO: make this agnostic as to the # of start hurdles
                if 0 <= msPassed < 1000:
                    self.displaysurf.blit(self.start_hurdles[0], (0, self.track.displaysurf_y_position))
                elif 1000 <= msPassed < 2000:
                    self.displaysurf.blit(self.start_hurdles[1], (0, self.track.displaysurf_y_position))
                elif msPassed > 3000:
                    self.started = True
        #Rest of game logic
        else: # Game is active
            self.track.current_displaysurf_x_position -= self.biker_1.speed
            self.biker_1.update_speed(self.biker_1.friction)
            self.biker_1.update_current_lane()
        # Handle inputs

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

        Input.keys.update_keys(events)

        if Input.keys.down(0):
            if self.lastEventStates[0] == False:
                self.biker_1.update_target_lane(-1)
        if Input.keys.down(1):
            if self.lastEventStates[1] == False:
                self.biker_1.update_target_lane(1)
        if Input.keys.down(2):
            self.biker_1.rotate_sprite_counter_clockwise()
        if Input.keys.down(3):
            self.biker_1.rotate_sprite_clockwise()
        if Input.keys.down(4):
            self.biker_1.update_speed(self.biker_1.acceleration_a)
        if Input.keys.down(5):
            self.biker_1.update_speed(self.biker_1.acceleration_b)
        if Input.keys.down(6):
            if self.heat > 0:
                self.heat -= 1
                pass
        if Input.keys.down(7):
            if self.heat < self.heatBarWidth:
                self.heat += 1
                pass
        #if events[8]    == True:
            #self.place_holder_escape()

        self.lastEventStates = events

        # Update Foreground Graphics
        #Biker
        self.displaysurf.blit(self.biker_1.sprite,
                              (0,
                               self.yPosForLane(self.biker_1.current_lane)))
        #Heat Bar
        heatBarRect = pygame.Rect(144 - self.heatBarWidth,
                                  209 - self.heatBarHeight,
                                  self.heatBarWidth,
                                  self.heatBarHeight)
        heatBarRect.width *= self.heat / self.heatBarWidth
        pygame.draw.rect(self.displaysurf,
                         pygame.Color("red"),
                         heatBarRect)

    def yPosForLane(self, lane):
        laneHeight = 12
        verticalOffset = 90
        return (lane * laneHeight) + verticalOffset

