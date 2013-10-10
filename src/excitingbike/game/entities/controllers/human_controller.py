class ArtificialIntelligenceController:
    def __init__(self, level):
        self.level = level
    
    # Controls a biker
    def control(self, biker):
        print("control biker by evaluating the input level object, seeing whose around you, and trying to navigate ahead of them")