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
        
        self.control_modes = {
            "keyboard" : {
                pygame.K_ESCAPE    : KEY_ESCAPE,
                pygame.K_UP        : KEY_UP,
                pygame.K_DOWN      : KEY_DOWN,
                pygame.K_LEFT      : KEY_LEFT,
                pygame.K_RIGHT     : KEY_RIGHT,
                pygame.K_z         : KEY_A_BUTTON,
                pygame.K_x         : KEY_B_BUTTON,
                pygame.K_RETURN    : KEY_START,
                pygame.K_RSHIFT    : KEY_SELECT,
                pygame.K_w         : KEY_UP,
                pygame.K_s         : KEY_DOWN,
                pygame.K_a         : KEY_LEFT,
                pygame.K_d         : KEY_RIGHT,
                pygame.K_SEMICOLON : KEY_A_BUTTON,
                pygame.K_QUOTE     : KEY_B_BUTTON
            },
            "joystick" : {

            }
        }
        pass

    def process_events(self):
        events = list()
        for new_event in pygame.event.get(pygame.KEYDOWN):
            if new_event.type == pygame.KEYDOWN:
                if new_event.key in self.control_modes["keyboard"]:
                    events.append(self.control_modes["keyboard"][new_event.key])
        return events


class KeyboardController(object):
    def process_events(self):
        pass
