import pygame

class Biker():
    # Initializes with a Bike controller
    def __init__(self):
        self.biker_sprite = pygame.image.load("assets/biker-sheet.gif").convert_alpha()
        self.displaysurf = self.biker_sprite.subsurface((264, 8, 20, 21))
        pass

    def update(self):
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

    # When in air - leans forward if possible
    def right(self):
        print("moving right")

    # Accelerates biker if not at max speed
    def accelerate(self):
        print("accelerating")

    # Brakes the bike if the bike is moving
    def brake(self):
        print("braking")
