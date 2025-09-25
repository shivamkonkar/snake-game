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
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size,cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):
            x = random.randint(0, number_of_cells-1)
            y = random.randint(0, number_of_cells-1)
            return Vector2(x, y)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()

        while position in snake_body:
            position = self.generate_random_cell()
        return position


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 8), Vector2(5, 8), Vector2(4, 8)]
        self.direction = Vector2(1,0)
        self.add_segment = False

    def draw(self):
        for segment in self.body:
            segment_rect = ( segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BROWN, segment_rect,0,7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        self.snake.update()
        self.check_collision_with_food()
    
    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            # self.score += 1
            # self.snake.eat_sound.play()



screen = pygame.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))
pygame.display.set_caption("Snake Legacy")
clock = pygame.time.Clock()
food_surface = pygame.image.load("food.png")
game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_d and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1, 0)    

    screen.fill(SAND)
    game.draw()
    pygame.display.update()
    clock.tick(60)
