import pygame
import math
class Hexagons():
    def __init__(self, screen):
        # Create all the Hexagons exactly as in the original game

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
    def calculate_vertices(self):
        vertices = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = 50 + self.side_length * math.cos(angle)
            y = 50 + self.side_length * math.sin(angle)
            vertices.append((x, y))
        return vertices
    def draw_hexagon(self,id, screen):
        hexagon = self.hexagons[id]
        pygame.draw.polygon(self.screen, self.blue,)



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
        
