import pygame
from screen import Screen
from ..game.gfx.track import Track
from ..input.input import Input

class LevelBuilderScreen(Screen):
    def __init__(self):
        super(LevelBuilderScreen,self).__init__()

        #Track objects todo move track objects to track class
        self.track = Track()
        self.track_location_index = 0
        self.current_track_surface = self.track.getThisTrack(self.track.level_builder_track)
        self.marker_surface_width = 8*self.screen_resolution
        self.marker_surface_height = self.marker_surface_width
        self.marker_surface = pygame.Surface((self.marker_surface_width,
                                              self.marker_surface_height))
        self.marker_surface.fill(self.DARKBLUE)

        #Menu objects
        self.BGCOLOR = self.BLACK
        self.options_surface_width = self.WINDOWWIDTH
        self.options_surface_height = 56*self.screen_resolution
        self.options_surface = pygame.Surface((self.options_surface_width,
                                               self.options_surface_height))
        self.options_surface.fill(self.BGCOLOR)
        self.not_hurdle_options = ["START1",
                                   "START2",
                                   "START3"]
        self.hurdle_options = self.track.hurdle_x_location_x_length.keys()
        for not_hurdle_option in self.not_hurdle_options:
            self.hurdle_options.remove(not_hurdle_option)
        self.hurdle_options_index = 0
        self.lastEventStates = [False,
                                False,
                                False,
                                False,
                                False,
                                False,
                                False,
                                False,
                                False,
                                ]
    ## TODO Update Biker Location Modules


    def options_index_left(self):
        self.hurdle_options_index -= 1

    def options_index_right(self):
        self.hurdle_options_index += 1

    def move_position_left(self):
        self.track_location_index += 16
        self.hurdle_options_index = self.hurdle_options.index(self.track.level_builder_track[(-self.track_location_index/16)+9])

    def move_position_right(self):
        self.track_location_index -= 16
        self.hurdle_options_index = self.hurdle_options.index(self.track.level_builder_track[(-self.track_location_index/16)+9])

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

        if Input.keys.down(1) == True:
            if self.lastEventStates[1] == False:
                self.options_index_left()
        if Input.keys.down(0) == True:
            if self.lastEventStates[0] == False:
                self.options_index_right()
        if Input.keys.down(2) == True:
            if self.lastEventStates[2] == False:
                self.move_position_left()
        if Input.keys.down(3) == True:
            if self.lastEventStates[3] == False:
                self.move_position_right()
        if Input.keys.down(4) == True:
            if self.lastEventStates[4] == False:
                self.place_holder_a()
        if Input.keys.down(5) == True:
            if self.lastEventStates[5] == False:
                self.place_holder_b()
        if Input.keys.down(6) == True:
            if self.lastEventStates[6] == False:
                self.place_holder_start()
        if Input.keys.down(7) == True:
            if self.lastEventStates[7] == False:
                self.place_holder_select()
        self.lastEventStates = events

        # loop hurdle option index if it tries to pass it's boundaries
        if self.hurdle_options_index < 0:
            self.hurdle_options_index = len(self.hurdle_options)-1
        elif self.hurdle_options_index == len(self.hurdle_options):
            self.hurdle_options_index = 0

        # Track State Update
        self.track.level_builder_track[(-self.track_location_index/16)+2] = self.hurdle_options[self.hurdle_options_index]
        self.current_track_surface = Track.getThisTrack(self.track, self.track.level_builder_track)

        ### Place Holder Background

        # Track Blit
        self.displaysurf.fill(self.LIGHTBLUE)
        self.displaysurf.blit(self.current_track_surface,
                              (self.track_location_index,
                               self.WINDOWHEIGHT-self.options_surface_height-self.track.TRACK_HEIGHT))
        self.displaysurf.blit(self.options_surface,
                              (0,
                               self.WINDOWHEIGHT-self.options_surface_height))
        self.displaysurf.blit(self.marker_surface,
                              (self.screen_resolution*64,
                               self.WINDOWHEIGHT-self.options_surface_height-8*self.screen_resolution))

        # Options Blit
        for i in range(len(self.hurdle_options)):
                if self.hurdle_options[i] == "BLANK":
                    self.fontsurface = (self.myfont.render(self.hurdle_options[i],
                                                           1,
                                                           self.WHITE))
                    self.displaysurf.blit(self.fontsurface,
                                          ((8*self.screen_resolution),
                                           190*self.screen_resolution))
                else:
                    self.fontsurface = (self.myfont.render(self.hurdle_options[i],
                                                           1,
                                                           self.WHITE))
                    self.displaysurf.blit(self.fontsurface,
                                          ((i*8*self.screen_resolution+40),
                                           190*self.screen_resolution))
        # Cursor Blit
        self.fontsurface = (self.myfont.render("^",
                                               1,
                                               self.WHITE))

        if self.hurdle_options_index == 0:
            self.displaysurf.blit(self.fontsurface,
                                  (((self.hurdle_options_index*8+24)*self.screen_resolution)
                                   ,200*self.screen_resolution))
        else:
            self.displaysurf.blit(self.fontsurface,
                                  (((self.hurdle_options_index*8+40)*self.screen_resolution),
                                   200*self.screen_resolution))
#        self.displaysurf.blit(self.surface, (x,y))
