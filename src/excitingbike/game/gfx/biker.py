import pygame

class Biker():
    # Initializes with a Bike controller
    def __init__(self):
        self.bikerWidth = 26
        self.bikerHeight = 26
        self.spriteMapX = 10 #0-19
        self.spriteMapY = 0  #0-13 not actually this simple
        self.biker_sprite = pygame.image.load("assets/biker-sheet.gif").convert_alpha()
                                                            #(min x location, min y location, x width, y height)
        self.displaysurf = self.biker_sprite.subsurface(((self.spriteMapX*self.bikerWidth),
                                                         3+(self.spriteMapY*self.bikerHeight),
                                                         self.bikerWidth,
                                                         self.bikerHeight))
        pass

    def update(self):
                                                            #(min x location, min y location, x width, y height)
        self.displaysurf = self.biker_sprite.subsurface(((self.spriteMapX*self.bikerWidth),
                                                         3+(self.spriteMapY*self.bikerHeight),
                                                         self.bikerWidth,
                                                         self.bikerHeight))
        pass

    # The following methods are used by Controllers

    # Simulates an up button presson
    def up(self):
        print("moving up")

    # Moves down one track, if possible.
    def down(self):
        print("moving down")

    # When in air - leans back if possible
    def left(self):
        print("moving left")
        self.spriteMapX += 1
        self.update()
    # When in air - leans forward if possible
    def right(self):
        print("moving right")
        self.spriteMapX -= 1
        self.update()
    # Accelerates biker if not at max speed
    def accelerate(self):
        print("accelerating")

    # Brakes the bike if the bike is moving
    def brake(self):
        print("braking")
