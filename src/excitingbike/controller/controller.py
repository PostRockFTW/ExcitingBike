import pygame
from excitingbike.locals import *


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
                pygame.locals.K_ESCAPE    : KEY_ESCAPE,
                pygame.locals.K_UP        : KEY_UP,
                pygame.locals.K_DOWN      : KEY_DOWN,
                pygame.locals.K_LEFT      : KEY_LEFT,
                pygame.locals.K_RIGHT     : KEY_RIGHT,
                pygame.locals.K_z         : KEY_A_BUTTON,
                pygame.locals.K_x         : KEY_B_BUTTON,
                pygame.locals.K_RETURN    : KEY_START,
                pygame.locals.K_RSHIFT    : KEY_SELECT,
                pygame.locals.K_w         : KEY_UP,
                pygame.locals.K_s         : KEY_DOWN,
                pygame.locals.K_a         : KEY_LEFT,
                pygame.locals.K_d         : KEY_RIGHT,
                pygame.locals.K_SEMICOLON : KEY_A_BUTTON,
                pygame.locals.K_QUOTE     : KEY_B_BUTTON
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
