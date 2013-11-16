import pygame

class Track(object):

    def __init__(self):
        self.track_sprite = pygame.image.load("assets/tracks.png").convert()

        self.track_hurdles = {
            "START1": (  10,  64),
            "START2": (  74,  64),
            "START3": ( 139,  64),
            "BLANK" : ( 202,  32),
            "A"     : ( 234,  32),
            "B"     : ( 266,  48),
            "C"     : ( 314,  80),
            "D"     : ( 394,  80),
            "E"     : ( 474,  48),
            "F"     : ( 522,  48),
            "G"     : ( 570,  48),
            "H"     : ( 618,  16),
            "I"     : ( 634,  16),
            "J"     : ( 650,  16),
            "K"     : ( 666,  32),
            "L"     : ( 698,  32),
            "M"     : ( 730,  16),
            "N"     : ( 746,  16),
            "O"     : ( 762, 208),
            "P"     : ( 970, 208),
            "Q"     : (1178,  96),
            "R"     : (1274, 208),
            "S"     : (1482, 224),
            "END"   : (1706,  96),
        }

        self.TRACK_HEIGHT = 112

        self.track_tints = [16+self.TRACK_HEIGHT*i for i in range(8)]

        self.tint = 0


    def getTrackHurdle(self, hurdleLetter):
        return self.track_sprite.subsurface((
            self.track_hurdles[hurdleLetter][0],
            self.track_tints[self.tint],
            self.track_hurdles[hurdleLetter][1],
            self.TRACK_HEIGHT
        ))
