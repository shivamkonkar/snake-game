import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((750,750))

pygame.display.set_caption("Snake Legacy")

clock = pygame.time.Clock()

while True:a
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
