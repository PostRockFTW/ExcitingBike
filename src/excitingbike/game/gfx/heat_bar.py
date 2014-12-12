import pygame

class Heat_bar():
    def __init__(self):
        self.heatBarWidth       = 31.0
        self.heatBarHeight      = 8.0
        self.heatBarBorderWith  = 1
        self.heat               = 0
        self.heatBarRect = pygame.Rect(144 - self.heatBarWidth,
                                  209 - self.heatBarHeight,
                                  self.heatBarWidth,
                                  self.heatBarHeight)
        self.heatBarRect.width *= self.heat / self.heatBarWidth

    def update_size(self,heat):
        self.heat = heat
        self.heatBarRect = pygame.Rect(144 - self.heatBarWidth,
                                  209 - self.heatBarHeight,
                                  self.heatBarWidth,
                                  self.heatBarHeight)
        self.heatBarRect.width *= self.heat / self.heatBarWidth
        return
