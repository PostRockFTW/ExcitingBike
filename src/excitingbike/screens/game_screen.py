import pygame

from ..game.gfx import track as Track
from ..game.gfx.biker import Biker
from ..game.gfx.track import Track
from ..game.gfx.heat_bar import Heat_bar
from screen import Screen
from ..locals import *
from ..input.input import Input


class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()

        # Set up instances for gamescreen objects

        #Initial state of the game
        self.game_state = "started"

        #State Surface???
        self.background_surface =  pygame.image.load("assets/Excitebike_BackGround.png").convert()

        #Track
        self.track = Track()

        #Biker
        self.biker_1 = Biker()

        #Heat Bar
        self.heat_bar = Heat_bar()

        #Intro Animation
        self.start_hurdles = [self.track.getTrackHurdle(hurdle) for hurdle in ("START1",
                                                                               "START2",
                                                                               "START3")]
        self.start_hurdle_width = self.start_hurdles[0].get_width()
        self.reset_game()

    def reset_game(self):
        self.started = False
        self.started_time = 0

    def blit_background(self):
        self.displaysurf.blit(self.background_surface, (0,0))
        self.displaysurf.blit(self.track.track_sprite,
                             (self.track.current_displaysurf_x_position,
                              self.track.displaysurf_y_position))
        self.displaysurf.blit(self.start_hurdles[-1],
                             (self.track.current_displaysurf_x_position,
                              self.track.displaysurf_y_position))

    def update_running_inputs(self,events):
        Input.keys.update_keys(events)
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
        # TODO add started, paused, and ending inputs
        if self.game_state == "started":
            pass
        elif self.game_state == "paused":
            pass
        elif self.game_state == "running":
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
                if self.biker_1.heat > 0:
                    self.biker_1.heat -= 1
                    pass
            if Input.keys.down(7):
                if self.biker_1.heat < self.heat_bar.heatBarWidth:
                    self.biker_1.heat += 1
                    pass
            #if events[8]    == True:
                #self.place_holder_escape()
        elif self.game_state == "ending":
            pass
        self.lastEventStates = events

    def starting(self):
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
                self.game_state = "running"

    def running(self,events):
        self.track.current_displaysurf_x_position -= self.biker_1.speed
        self.biker_1.track_x += self.biker_1.speed
        self.biker_1.update_speed(self.biker_1.friction)
        self.biker_1.update_current_lane()
        self.heat_bar.update_size(self.biker_1.heat)

    def blit_forground(self):
        #Biker
        self.displaysurf.blit(self.biker_1.sprite,
                              (0,
                               self.yPosForLane(self.biker_1.current_lane)))
        #Heat Bar
        pygame.draw.rect(self.displaysurf,
                         pygame.Color("red"),
                         self.heat_bar.heatBarRect)

    def update(self, events, states):
        #Update Background gfx to wipe screen
        self.blit_background()
        self.update_running_inputs(events)
        if self.game_state == "started":
            self.starting()
        elif self.game_state == "running":
            self.running(events)
        self.blit_forground()

    def yPosForLane(self, lane):
        laneHeight = 12
        screen_offset = 90
        return (lane * laneHeight) + screen_offset - self.track.game_track_y_array[int(self.biker_1.track_x)]

