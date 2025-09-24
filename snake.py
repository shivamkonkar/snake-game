import pygame
import sys
from pygame.math import Vector2

pygame.init()

SAND = (237, 201, 175)
BROWN = (101, 67, 33)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = Vector2(5,2)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size,cell_size)
        screen.blit(food_surface, food_rect)

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
