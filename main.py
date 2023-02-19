import pygame
import random
import math
from planet import Planet
from comet import Comet
from galaxy import Galaxy

# Define game constants
WIDTH = 1024
HEIGHT = 1024
DIRECTIONS = list(range(360))
GRAVITY_CONST = 10
NUM_PLANETS = 5  # number of planets to generate

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Galaxy")
clock = pygame.time.Clock()

# Create Galaxy object with planets
galaxy = Galaxy(NUM_PLANETS, WIDTH, HEIGHT)

# Game loop
comets = []
running = True
while running:
    clock.tick(30)  # limit frame rate to 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Create new comet on left mouse click
            x, y = event.pos
            comets.append(Comet(x, y))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset game on 'R' key press
                comets = []
                galaxy.clear()
                galaxy.generate()

    # Update comet positions
    for comet in comets:
        comet.update(galaxy.planets, comets)
        if comet.is_outside(WIDTH, HEIGHT):
            comets.remove(comet)


    # Draw objects
    screen.fill((0, 0, 0))
    for planet in galaxy.planets:
        planet.draw(screen)
    for comet in comets:
        comet.draw(screen)
    pygame.display.flip()

# Quit Pygame on exit
pygame.quit()