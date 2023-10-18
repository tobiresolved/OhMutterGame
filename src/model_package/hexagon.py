import pygame
import math
import sys
import numpy as np
class Hexagons():
    def __init__(self, screen):
        # Create all the Hexagons exactly as in the original game
        sys.path.append("C:\\Users\\tobia\\OneDrive\\Desktop\\Programmierprojekte\\OhMutterGame\\src")

        self.hexagons = {}
        self.hexagons[1] = Hexagon(id=1, top_num=1, top_right_num=6, bottom_right_num=5, bottom_num=3,bottom_left_num=2,top_left_num=4)
        self.hexagons[2] = Hexagon(id=2, top_num=1, top_right_num=2, bottom_right_num=3, bottom_num=4,bottom_left_num=5,top_left_num=6)
        self.hexagons[3] = Hexagon(id=3, top_num=1, top_right_num=6, bottom_right_num=4, bottom_num=2,bottom_left_num=5,top_left_num=3)
        self.hexagons[4] = Hexagon(id=4, top_num=1, top_right_num=6, bottom_right_num=5, bottom_num=4,bottom_left_num=3,top_left_num=2)
        self.hexagons[5] = Hexagon(id=5, top_num=1, top_right_num=4, bottom_right_num=3, bottom_num=6,bottom_left_num=5,top_left_num=2)
        self.hexagons[6] = Hexagon(id=6, top_num=1, top_right_num=6, bottom_right_num=2, bottom_num=4,bottom_left_num=5,top_left_num=3)
        self.hexagons[7] = Hexagon(id=7, top_num=1, top_right_num=4, bottom_right_num=6, bottom_num=2,bottom_left_num=3,top_left_num=5)

        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.side_length = 50
        self.screen = screen

    def draw_regular_polygon(self, screen):
        corners, radius = 6, 70
        print((radius * math.cos(180/corners)))
        x, y = (900 - radius - 20), np.round(700  - (radius * (math.cos(math.pi/corners))) - 20)
        print(x)
        print(y)
        width = 0  # If width = 0, it will fill the polygon
        y_height = 10
        pygame.draw.polygon(screen, self.blue, [(x + radius * math.cos(2 * math.pi * i / corners), y + radius * math.sin(2 * math.pi * i / corners)) for i in range(corners)], width)





class Hexagon(Hexagons):
    def __init__(self, id, top_num,top_right_num ,bottom_right_num,bottom_num,bottom_left_num,top_left_num):
        # The ID ranges from [1,7] and is used to distinguish the different Hexagons
        # The position is used to initialize the Hexagons for the first time. t -> top | b -> bottom | tr -> top right | bl -> bottom left | ...
        self.id = id
        self.pos_t = top_num
        self.pos_tr = top_right_num
        self.pos_br = bottom_right_num
        self.pos_b = bottom_num
        self.pos_bl = bottom_left_num
        self.pos_tl = top_left_num
        
