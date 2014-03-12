import pygame
from ..locals import *


# Inputs to ExciteBike:

# four directions (up, down, left, right)
#    up/down = change lane
#    left/right = change angle while in air
# A/B
#   a = accelerate
#   b = overheat accelerate

class Controller(object):

    def __init__(self):

        self.default_controls = {
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
        self.custom_controls = {
            "keyboard": {

            },
            "joystick": {

            }
        }

    def get_mapped_key(self, key):
        if key in self.custom_controls['keyboard']:
            return self.custom_controls['keyboards'][key]
        elif key in self.default_controls['keyboard']:
            return self.default_controls['keyboard'][key]
        else:
            return None


    def process_events(self):
        events = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                events.append(EVENT_QUIT)
            elif event.type == pygame.KEYDOWN:
                mapped_key = self.get_mapped_key(event.key)
                if mapped_key is not None:
                    events.append(mapped_key)

        return events


class KeyboardController(object):
    def process_events(self):
        pass
