class Biker(pygame.sprite.Sprite):
    # Initializes with a Bike controller
    def __init__(self, controller):
        self.controller = controller
        
    def update(self):
        self.controller.control(self)
    
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
        print("moving left")
    
    # Accelerates biker if not at max speed
    def accelerate(self):
        print("accelerating")
    
    # Brakes the bike if the bike is moving
    def brake(self):
        print("braking")