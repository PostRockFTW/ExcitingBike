class Keyboard(object):
    
    def __init__(self):
        self.current_keys = []
        self.previous_keys = []
    
    def update_keys(self, keys):
        self.previous_keys = self.current_keys
        self.current_keys = keys
    
    def down(self, key_code):
        return self.current_keys[key_code]
        
    def up(self, key_code):
        return not self.current_keys[key_code]
        
    def pressed(self, key_code):
        # If the key is released (i.e. current_keys doesn't have it
        # and the previous_keys has it, then it was pressed.
        return not self.current_keys[key_code] and self.previous_keys[key_code]
