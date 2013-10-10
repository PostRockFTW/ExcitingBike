class Tile(pygame.sprite.Sprite):
    def __init__(self):
        print("Tile created")
        
    # Returns true if the tile contacts the biker, otherwise false
    def contacts(self, biker):
        print("contacts")