import pygame
import sys

pygame.init()

SAND = (237, 201, 175)   # Define a light sand color using RGB values
BROWN = (101, 67, 33)    # Define a brown color using RGB values

screen = pygame.display.set_mode((750,750))

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SAND)  # Fill the screen background with the sand color
    pygame.display.update()
    clock.tick(60)
