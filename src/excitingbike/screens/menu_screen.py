from screen import Screen
from ..locals import *

class MenuScreen(Screen):
    def __init__(self):

        super(MenuScreen,self).__init__()

        # Menu logic variables

        self.menu_options_index = 0
        self.menu_options = ["none"]
        self.menu_options_dictionary = []
        self.selection = self.menu_options[self.menu_options_index]
        self.blink_speed = 8
        self.blink_counter = 0
        self.blink_state = True
        self.blink_color = self.RED

    # Abilities all menus should have

    def set_menu_options(self,arg):
        self.menu_options=arg
        self.update_selection()

    def update_selection(self):
        self.selection = self.menu_options[self.menu_options_index]

    def go_down(self):
        self.menu_options_index += 1
        if self.menu_options_index >= len(self.menu_options):
            self.menu_options_index = 0
        self.update_selection()

    def go_up(self):
        self.menu_options_index -= 1
        if self.menu_options_index < 0:
            self.menu_options_index += len(self.menu_options)
        self.update_selection()

    def update(self,events,states):

            # Event Operations

            # FROM LOCALS
            #KEY_UP       = 0
            #KEY_DOWN     = 1
            #KEY_LEFT     = 2
            #KEY_RIGHT    = 3
            #KEY_A_BUTTON = 4
            #KEY_B_BUTTON = 5
            #KEY_START    = 6
            #KEY_SELECT   = 7
            #KEY_ESCAPE   = 8
            if events[1] == True:
                if self.lastEventStates[1] == False:
                    self.go_down()
            elif events[0] == True:
                if self.lastEventStates[0] == False:
                    self.go_up()
            elif events[4] == True:
                states.append(self.menu_options_dictionary[self.selection])
            self.lastEventStates = events
            # Logic for blinking selection

            self.blink_counter += 1
            if self.blink_counter > self.blink_speed:
                self.blink_state = not self.blink_state
                self.blink_counter = 0
            if self.blink_state:
                self.blink_color = self.WHITE
            else:
                self.blink_color = self.RED

            # fill the screen with stuff to be updated

            ### Background and logo

            self.displaysurf.fill(self.BGCOLOR)

            ### Menu Options

            for i in range(len(self.menu_options)):
                if i == self.menu_options_index:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.blink_color))
                else:
                    self.fontsurface = (self.myfont.render(self.menu_options[i], 1, self.WHITE))
                self.displaysurf.blit(self.fontsurface, (75, (138+i*12)))
