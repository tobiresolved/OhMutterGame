import pygame
import sys
from model_package.hexagon import Hexagon
from model_package.hexagon import Hexagons
sys.path.append("C:\\Users\\tobia\\OneDrive\\Projects\\OhMutter\\src\\model_package")

pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((900, 700))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hex = Hexagon()


   

    pygame.display.flip()

pygame.quit()