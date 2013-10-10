# Runs the main loop of the program
class Runner:
    def __init__(self, initial_screen):
        self.screen = initial_screen
    
    def run(self):
        while(True):
            self.screen.update()