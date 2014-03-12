import game_screen
from menu_screen import MenuScreen


class OptionMenuScreen(MenuScreen):
    def __init__(self):

        super(OptionMenuScreen,self).__init__()

        self.set_menu_options(("INPUT OPTIONS", "AUDIO OPTIONS", "VIDEO OPTIONS"))
        self.menu_options_dictionary = {"INPUT OPTIONS":game_screen.GameScreen, "AUDIO OPTIONS":game_screen.GameScreen, "VIDEO OPTIONS":game_screen.GameScreen}

def update(self,events,states):

            super(MainMenuScreen,self).update(events,states)