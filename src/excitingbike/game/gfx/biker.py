import pygame

class Biker():
    # Initializes with a Bike controller
    def __init__(self):

        ###Biker gfx
        self.sprite_width = 26
        self.sprite_height = 26
        self.sprite_map_x = 10 #0-19
        self.sprite_map_y = 0  #0-13 not actually this simple
        self.sprite_map = pygame.image.load("assets/biker-sheet.gif").convert_alpha()
                                                #(min x location, min y location, x width, y height)
        self.sprite = self.sprite_map.subsurface(((self.sprite_map_x*self.sprite_width),
                                                         3+(self.sprite_map_y*self.sprite_height),
                                                         self.sprite_width,
                                                         self.sprite_height))
        ###Biker physics
        #Speed
        self.friction       = -0.1
        self.acceleration_a = .2
        self.acceleration_b = 1
        self.speed    = 0
        self.max_speed = 4
        self.lane_change_speed = .2

        #Location
        self.min_lane_range   = 1
        self.max_lane_range   = 4
        self.lane_range  = (self.min_lane_range, self.max_lane_range)
        self.current_lane = 2
        self.targetLane = 2

        #Angle

        #State


        pass

    def update_gfx(self):
                                                            #(min x location, min y location, x width, y height)
        self.sprite = self.sprite_map.subsurface(((self.sprite_map_x*self.sprite_width),
                                                         3+(self.sprite_map_y*self.sprite_height),
                                                         self.sprite_width,
                                                         self.sprite_height))

    # When in air - leans back if possible
    def rotate_sprite_counter_clockwise(self):
        if self.sprite_map_x < 15:
            self.sprite_map_x += 1
            self.update_gfx()

    # When in air - leans forward if possible
    def rotate_sprite_clockwise(self):
        if self.sprite_map_x > 10:
            self.sprite_map_x -= 1
            self.update_gfx()

    def update_speed(self, acceleration):
        self.speed += acceleration
        self.speed = max(0,
                         min(self.speed, self.max_speed))

    def update_target_lane(self, numeric_difference):
        self.targetLane += numeric_difference
        self.targetLane = max(self.min_lane_range,
                              min(self.max_lane_range, self.targetLane))
    def update_current_lane(self):
        self.direction = -1 if self.current_lane > self.targetLane else 1
        if abs(self.current_lane - self.targetLane) > 0.01:
            self.current_lane += self.direction * self.lane_change_speed