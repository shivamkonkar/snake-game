import pygame
import sys
from pygame.math import Vector2
import random   # Added: Import random to generate random food positions

pygame.init()

SAND = (237, 201, 175)
BROWN = (101, 67, 33)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.generate_random_pos()   # Updated: Instead of fixed (5,2), now food spawns at a random position

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size,cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_pos(self):   # Added: Function to create a random position for food
        x = random.randint(0, number_of_cells - 1 )   # Added: Pick random x within grid bounds
        y = random.randint(0, number_of_cells - 1 )   # Added: Pick random y within grid bounds
        position = Vector2(x,y)   # Added: Store (x,y) as a Vector2 object
        return position   # Added: Return the random position

screen = pygame.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()
food = Food()
food_surface = pygame.image.load("food.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SAND)
    food.draw()
    pygame.display.update()
    clock.tick(60)

