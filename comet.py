import pygame
import random
import math

# Define game constants
COMET_RADIUS = 5
COMET_SPEED = 5
DIRECTIONS = list(range(360))
GRAVITY_CONST = 10
TAIL_LENGTH = 20
TAIL_WIDTH = 3

class Comet:
    def __init__(self, x, y, game_width, game_height):
        self.x = x
        self.y = y
        self.direction = random.choice(DIRECTIONS)
        self.history = []  # list of previous positions
        self.mass = COMET_RADIUS * 10  # set mass to 10 times the comet diameter
        self.game_width = game_width
        self.game_height = game_height

    def update(self, planets, comets):
        # Calculate movement vector
        dx = math.cos(math.radians(self.direction)) * COMET_SPEED
        dy = math.sin(math.radians(self.direction)) * COMET_SPEED

        # Calculate gravitational force from planets
        for planet in planets:
            distance = math.sqrt((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2)
            force = GRAVITY_CONST * self.mass * planet.mass / distance ** 2
            angle = math.atan2(planet.y - self.y, planet.x - self.x)

            # Update movement vector with gravitational force
            dx += math.cos(angle) * force / self.mass
            dy += math.sin(angle) * force / self.mass

            # Check if comet has collided with planet
            if distance < planet.radius:
                planet.mass += self.mass  # add comet mass to planet
                comets.remove(self)  # remove comet from active list

        # Update position
        self.x += dx
        self.y += dy

        # Add current position to history
        self.history.append((self.x, self.y))

        # Remove old positions from history
        if len(self.history) > TAIL_LENGTH:
            self.history.pop(0)

        # Check if comet is outside game area and remove it
        if self.x < -COMET_RADIUS or self.x > self.game_width + COMET_RADIUS or \
           self.y < -COMET_RADIUS or self.y > self.game_height + COMET_RADIUS:
            comets.remove(self)

    def draw(self, surface):
        # Create comet surface with tail and draw onto main surface
        comet_surf = pygame.Surface((COMET_RADIUS*2, COMET_RADIUS*2 + TAIL_LENGTH), pygame.SRCALPHA)
        pygame.draw.circle(comet_surf, (255, 255, 255), (COMET_RADIUS, COMET_RADIUS), COMET_RADIUS)

        # Draw tail
        for i, pos in enumerate(self.history):
            alpha = int(255 * (1 - i/TAIL_LENGTH))  # fade out tail
            color = (255, 255, 255, alpha)
            x, y = pos
            pygame.draw.rect(comet_surf, color, (COMET_RADIUS-TAIL_WIDTH//2, COMET_RADIUS*2+i, TAIL_WIDTH, 1))

        # Draw comet with tail
        surface.blit(comet_surf, (self.x - COMET_RADIUS, self.y - COMET_RADIUS*2 - TAIL_LENGTH))


class Planet:
    def __init__(self, x, y, radius, game_width, game_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = math.pi * radius ** 2 * 10  # set mass to
