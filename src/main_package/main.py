import pygame
import sys
sys.path.append("C:\\Users\\tobia\\OneDrive\\Desktop\\Programmierprojekte\\OhMutterGame\\src")
from model_package.hexagon import Hexagons


def main():
    

    
    pygame.init()

# Create a Pygame window
    screen = pygame.display.set_mode((900, 700))
    hex = Hexagons(screen=screen)

    running = True
    while running:
        hex.draw_regular_polygon(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


   

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


