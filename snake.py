import pygame
import sys
from pygame.math import Vector2    # Import Vector2 to represent positions with x, y coordinates

pygame.init()

SAND = (237, 201, 175)
BROWN = (101, 67, 33)

cell_size = 30        # Define the size of each grid cell (in pixels)
number_of_cells = 25  # Define how many cells fit on one side of the grid

class Food:  # Create a Food class to represent the food object
    def __init__(self):
        self.position = Vector2(5,2)  # Food starts at grid position (5,2) using Vector2

    def draw(self):
        # Create a rectangle for food at its position scaled by cell_size
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)  # Draw the food image on the screen at that rectangle

screen = pygame.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))  
# Create the game window sized according to cell size × number of cells

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()
food = Food()  # Create a Food object
food_surface = pygame.image.load("food.png")  # Load the image used for food

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SAND)
    food.draw()
    pygame.display.update()
    clock.tick(60)
