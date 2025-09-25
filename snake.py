import pygame  # Import pygame library for game development
import sys     # Import sys to handle exiting the program

pygame.init()  # Initialize all pygame modules

# Create a display window of 750x750 pixels
screen = pygame.display.set_mode((750,750))

# Set the window title
pygame.display.set_caption("Snake Legacy")

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop (runs continuously until the game is closed)
while True:  
    # Handle all events (like quit, keypress, mouse events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the close button is clicked
            pygame.quit()              # Quit pygame
            sys.exit()                 # Exit the program safely

    pygame.display.update()  # Refresh the screen with any changes
    clock.tick(60)           # Run the loop at 60 frames per second

