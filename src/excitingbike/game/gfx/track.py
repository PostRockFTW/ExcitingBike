import pygame
from collections import OrderedDict

track_sprite = None

track_hurdles = OrderedDict([
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

TRACK_HEIGHT = 112

track_tints = [16 + TRACK_HEIGHT*i for i in range(8)]

tint = 0


def getTrackSprite():
    global track_sprite
    if track_sprite is None:
        track_sprite = pygame.image.load("assets/tracks.png").convert()
    return track_sprite

def getTrackHurdle(hurdleLetter):
    return getTrackSprite().subsurface((
        track_hurdles[hurdleLetter][0],
        track_tints[tint],
        track_hurdles[hurdleLetter][1],
        TRACK_HEIGHT
    ))

def getThisTrack(track_list):
    track_surface_array = [getTrackHurdle(hurdle_surface) for hurdle_surface in track_list]
    track_width = sum((surface.get_width() for surface in track_surface_array))
    track_surface = pygame.Surface((track_width,TRACK_HEIGHT))
    width_counter = 0
    for surface in track_surface_array:
        track_surface.blit(surface, (width_counter,0))
        width_counter += surface.get_width ()
    return track_surface
