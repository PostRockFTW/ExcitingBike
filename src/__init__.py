import pygame
from pygame.locals import *

from excitingbike.screens.intro_screen import IntroScreen
from runner import Runner

pygame.init()
pygame.font.init()
intro_screen = IntroScreen()
runner = Runner(intro_screen)
runner.run()