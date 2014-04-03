import pygame
from screen import Screen
from ..game.gfx import track as Track
from ..locals import *

class LevelBuilderScreen(Screen):
    def __init__(self):
        super(LevelBuilderScreen,self).__init__()
        self.location_index = 0
        self.BGCOLOR = self.BLACK
#Track objects
        self.current_track_list = ["START1","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","BLANK","END"]
        self.current_track_surface = Track.getThisTrack(self.current_track_list)
        self.marker_surface_width = 8*self.SCREEN_MAGNIFIER
        self.marker_surface_height = self.marker_surface_width
        self.marker_surface = pygame.Surface((self.marker_surface_width, self.marker_surface_height))
        self.marker_surface.fill(self.DARKBLUE)
#Menu objects
        self.options_surface_width = self.WINDOWWIDTH
        self.options_surface_height = 56*self.SCREEN_MAGNIFIER
        self.options_surface = pygame.Surface((self.options_surface_width,self.options_surface_height))
        self.options_surface.fill(self.BGCOLOR)
        self.not_hurdle_options = ["START1", "START2", "START3", "END"]
        self.hurdle_options = Track.track_hurdles.keys()
        for not_hurdle_option in self.not_hurdle_options:
            self.hurdle_options.remove(not_hurdle_option)
        self.hurdle_options_index = 0
        self.highlighted_track = ((self.location_index/16)+9)
    ## TODO Update Biker Location Modules
    def options_index_left(self):
        self.hurdle_options_index -= 1

    def options_index_right(self):
        self.hurdle_options_index += 1

    def move_position_left(self):
        self.location_index += 16
        self.highlighted_track = (-self.location_index/16)+9

    def move_position_right(self):
        self.location_index -= 16
        self.highlighted_track = (-self.location_index/16)+9

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
                self.options_index_left()
            elif event == KEY_UP:
                self.options_index_right()
            elif event == KEY_LEFT:
                self.move_position_left()
            elif event == KEY_RIGHT:
                self.move_position_right()
            elif event == KEY_A_BUTTON:
                self.place_holder_a()
            elif event == KEY_B_BUTTON:
                self.place_holder_b()
            elif event == KEY_START:
                self.place_holder_start()
            elif event == KEY_SELECT:
                self.place_holder_select()

        # Track State Update
        if self.hurdle_options_index < 0:
            self.hurdle_options_index = len(self.hurdle_options)-1
        elif self.hurdle_options_index == len(self.hurdle_options):
            self.hurdle_options_index = 0
        self.hurdle_option_index = self.highlighted_track
        self.current_track_list[self.highlighted_track] = self.hurdle_options[self.hurdle_options_index]
        self.current_track_surface = Track.getThisTrack(self.current_track_list)

        ### Place Holder Background

        # Track Blit
        self.displaysurf.fill(self.LIGHTBLUE)
        self.displaysurf.blit(self.current_track_surface, (self.location_index,self.WINDOWHEIGHT-self.options_surface_height-Track.TRACK_HEIGHT))
        self.displaysurf.blit(self.options_surface, (0,self.WINDOWHEIGHT-self.options_surface_height))
        self.displaysurf.blit(self.marker_surface, (self.SCREEN_MAGNIFIER*64,self.WINDOWHEIGHT-self.options_surface_height-8*self.SCREEN_MAGNIFIER))

        # Options Blit
        for i in range(len(self.hurdle_options)):
                if self.hurdle_options[i] == "BLANK":
                    self.fontsurface = (self.myfont.render(self.hurdle_options[i], 1, self.WHITE))
                    self.displaysurf.blit(self.fontsurface, ((8*self.SCREEN_MAGNIFIER),190*self.SCREEN_MAGNIFIER))
                else:
                    self.fontsurface = (self.myfont.render(self.hurdle_options[i], 1, self.WHITE))
                    self.displaysurf.blit(self.fontsurface, ((i*8*self.SCREEN_MAGNIFIER+80),190*self.SCREEN_MAGNIFIER))
        # Cursor Blit
        self.fontsurface = (self.myfont.render("^", 1, self.WHITE))

        if self.hurdle_options_index == 0:
            self.displaysurf.blit(self.fontsurface, (((self.hurdle_options_index*8+24)*self.SCREEN_MAGNIFIER),200*self.SCREEN_MAGNIFIER))
        else:
            self.displaysurf.blit(self.fontsurface, (((self.hurdle_options_index*8+40)*self.SCREEN_MAGNIFIER),200*self.SCREEN_MAGNIFIER))
#        self.displaysurf.blit(self.surface, (x,y))
