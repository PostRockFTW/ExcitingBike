import pygame
from collections import OrderedDict

class Track():
    def __init__(self):
        self.track_sprite = None

        self.track_hurdles = OrderedDict([
            ("START1", (  10,  64)),
            ("START2", (  74,  64)),
            ("START3", ( 139,  64)),
            ("BLANK" , ( 202,  32)),
            ("A"     , ( 234,  32)),
            ("B"     , ( 266,  48)),
            ("C"     , ( 314,  80)),
            ("D"     , ( 394,  80)),
            ("E"     , ( 474,  48)),
            ("F"     , ( 522,  48)),
            ("G"     , ( 570,  48)),
            ("H"     , ( 618,  16)),
            ("I"     , ( 634,  16)),
            ("J"     , ( 650,  16)),
            ("K"     , ( 666,  32)),
            ("L"     , ( 698,  32)),
            ("M"     , ( 730,  16)),
            ("N"     , ( 746,  16)),
            ("O"     , ( 762, 208)),
            ("P"     , ( 970, 208)),
            ("Q"     , (1178,  96)),
            ("R"     , (1274, 208)),
            ("S"     , (1482, 224)),
            ("END"   , (1706,  96)),
            ])

        self.TRACK_HEIGHT = 112

        self.track_tints = [16 + self.TRACK_HEIGHT*i for i in range(8)]

        self.tint = 0

    def getTrackSprite(self):
        if self.track_sprite is None:
           self.track_sprite = pygame.image.load("assets/tracks.png").convert()
        return self.track_sprite

    def getTrackHurdle(self,hurdleLetter):
        return self.getTrackSprite().subsurface((
            self.track_hurdles[hurdleLetter][0],
            self.track_tints[self.tint],
            self.track_hurdles[hurdleLetter][1],
            self.TRACK_HEIGHT
        ))

    def getThisTrack(self,track_list):
        self.track_surface_array = [self.getTrackHurdle(hurdle_surface) for hurdle_surface in track_list]
        self.track_width = sum((surface.get_width() for surface in self.track_surface_array))
        self.track_surface = pygame.Surface((self.track_width,self.TRACK_HEIGHT))
        self.width_counter = 0
        for surface in self.track_surface_array:
            self.track_surface.blit(surface, (self.width_counter,0))
            self.width_counter += surface.get_width ()
        return self.track_surface
