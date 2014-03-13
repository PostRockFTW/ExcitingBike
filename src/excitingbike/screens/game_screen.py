import pygame

from ..game.entities import track
from screen import Screen


class GameScreen(Screen):

    def __init__(self):
        super(GameScreen,self).__init__()
        self.BGCOLOR = self.RED

        self.temporary_track_list = ["BLANK","BLANK","BLANK","A","G","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK","BLANK","BLANK","BLANK","D","D","BLANK","BLANK","B","BLANK","BLANK"]

        self.start_hurdles = [track.getTrackHurdle(hurdle) for hurdle in ("START1", "START2", "START3")]
        self.start_hurdle_width = self.start_hurdles[0].get_width()

        self.track_surface = self.loadLevel(self.temporary_track_list)

        self.resetGame()

        self.currentOffset = 0
        self.bikerSpeed = 4

    def loadLevel(self, trackList):

        track_hurdles = [track.getTrackHurdle(hurdle) for hurdle in trackList]
        track_width = sum((surface.get_width() for surface in track_hurdles))
        track_height = track_hurdles[0].get_height()
        track_surface = pygame.Surface((track_width, track_height))

        # For now, just blit the hurdles to the level once
        xPos = self.start_hurdle_width
        for surface in track_hurdles:
            track_surface.blit(surface, (xPos, 0))
            xPos += surface.get_width()

        return track_surface

    def resetGame(self):
        self.started = False
        self.started_time = 0

    def update(self, events, states):

        self.displaysurf.blit(self.track_surface, (self.currentOffset, 0))

        self.displaysurf.blit(self.start_hurdles[-1], (self.currentOffset, 0))

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

