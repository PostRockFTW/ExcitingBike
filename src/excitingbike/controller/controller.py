import pygame

KEY_UP    = 0
KEY_DOWN  = 1
KEY_LEFT  = 2
KEY_RIGHT = 3
BACK      = 4
QUIT      = 5


# Inputs to ExciteBike:

# four directions (up, down, left, right)
#    up/down = change lane
#    left/right = change angle while in air
# A/B
#   a = accelerate
#   b = overheat accelerate

class Controller(object):

    def __init__(self):
        self.control_mode = "keyboard"

        self.control_modes = {
            "keyboard" : {
                pygame.locals.K_UP    : KEY_UP,
                pygame.locals.K_DOWN  : KEY_DOWN,
                pygame.locals.K_LEFT  : KEY_LEFT,
                pygame.locals.K_RIGHT : KEY_RIGHT,
                pygame.locals.K_w : KEY_UP
            },
            "joystick" : {

            }
        }
        pass

    def process_events(self):
        return [self.control_modes[self.control_mode][new_event.key] for new_event in pygame.event.get(pygame.locals.KEYDOWN)]


class KeyboardController(object):
    def process_events(self):
        pass
