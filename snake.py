import pygame
import sys
from pygame.math import Vector2
import random

pygame.init()

SAND = (237, 201, 175)
BROWN = (101, 67, 33)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.generate_random_pos()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size,cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1 )
        y = random.randint(0, number_of_cells - 1 )
        position = Vector2(x,y)
        return position


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 8), Vector2(5, 8), Vector2(4, 8)]   # Snake starts with 3 segments

    def draw(self):
        for segment in self.body:   # Loop through all snake segments
            segment_rect = ( segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)   # Position and size of each segment
            pygame.draw.rect(screen, BROWN, segment_rect,0,7)   # Draw each segment as a brown rounded rectangle


screen = pygame.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()
food = Food()
food_surface = pygame.image.load("food.png")

snake = Snake()   # Create a snake object

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SAND)
    food.draw()
    snake.draw()   # Draw the snake on screen
    pygame.display.update()
    clock.tick(60)
