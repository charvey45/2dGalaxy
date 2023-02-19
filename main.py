import pygame
import random
from planet import Planet
from comet import Comet

# Initialize Pygame
pygame.init()

# Define game constants
WIDTH = 1024
HEIGHT = 1024
COMET_RADIUS = 5
COMET_SPEED = 5
DIRECTIONS = list(range(360))
GRAVITY_CONST = 10
TAIL_LENGTH = 20
TAIL_WIDTH = 3
PLANET_RADIUS = 50

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Galaxy")

# Create planet objects
planets = [Planet(WIDTH//4, HEIGHT//2, PLANET_RADIUS, WIDTH, HEIGHT),
           Planet(WIDTH*3//4, HEIGHT//2, PLANET_RADIUS, WIDTH, HEIGHT)]

# Create empty list to store comets
comets = []

# Start game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Create new comet on mouse click
            x, y = pygame.mouse.get_pos()
            comets.append(Comet(x, y, WIDTH, HEIGHT))

    # Fill screen with black
    #screen.fill((0, 0, 0))

    # Update and draw planets
    for planet in planets:
        planet.draw(screen)

    # Update and draw comets
    for comet in comets:
        comet.update(planets, comets)
        comet.draw(screen)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
