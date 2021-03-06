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

    events = set([])
    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events.add(EVENT_QUIT)
            elif event.type == pygame.KEYDOWN:
                mapped_key = self.get_mapped_key(event.key)
                if mapped_key is not None:
                    self.events.add(mapped_key)
            elif event.type == pygame.KEYUP:
                mapped_key = self.get_mapped_key(event.key)
                if mapped_key is not None:
                    self.events.remove(mapped_key)
        self.eventStates = [False for i in range(9)]#number of input types ##Todo make this reflexive to max(events)
        for i in self.events: #Event Types are stored as numbers starting at 0
            self.eventStates[i] = True
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
        return self.eventStates


class KeyboardController(object):
    def process_events(self):
        pass
