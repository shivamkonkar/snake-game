import pygame
import sys

pygame.init()

SAND = (237, 201, 175)
BROWN = (101, 67, 33)

screen = pygame.display.set_mode((750,750))

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SAND)
    pygame.display.update()
    clock.tick(60)
