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
    def __init__(self, snake_body):   # Food now takes snake_body so it can avoid spawning on the snake
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size,cell_size)
        screen.blit(food_surface, food_rect)
        
    def generate_random_pos(self):   # Signature changed to match constructor
        x = random.randint(0, number_of_cells - 1 )
        y = random.randint(0, number_of_cells - 1 )
        position = Vector2(x,y)


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 8), Vector2(5, 8), Vector2(4, 8)]
        self.direction = Vector2(1,0)

    def draw(self):
        for segment in self.body:
            segment_rect = ( segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BROWN, segment_rect,0,7)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)


class Game:   # New class added to organize Snake and Food together
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)   # Food created with snake body passed in

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        self.snake.update()


screen = pygame.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))
pygame.display.set_caption("Snake Legacy")
clock = pygame.time.Clock()
food_surface = pygame.image.load("food.png")
game = Game()   # Using Game object instead of separate snake and food
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()   # Update through Game class

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and game.snake.direction != Vector2(0,1):   # Snake accessed via game.snake
                game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_d and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1, 0)    

    screen.fill(SAND)
    game.draw()   # Draw handled by Game class
    pygame.display.update()
    clock.tick(60)
