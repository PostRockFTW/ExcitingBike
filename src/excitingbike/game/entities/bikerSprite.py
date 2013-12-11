import pygame

class BikerSprite(object):

    def __init__(self):
        self.biker_sprite =  pygame.image.load("assets/biker-sheet.png").convert()

        self.bikers = (
            (259, 20), # forward 1
            (285, 19), # forward 2
            (310, 20), # up 1

        )

        self.biker_height = 24
        self.biker_tints = (28)
        self.tint = 0

    def getBikerSprite(self, bikerPose):
        return self.biker_sprite.subsurface((
            self.bikers[bikerPose][0],
            self.biker_tints[self.tint],
            self.bikers[bikerPose][1],
            self.biker_height
        ))
        pass
