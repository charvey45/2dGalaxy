import pygame
import random
class Planet:

    def __init__(self, x, y, radius,mass, color, game_width, game_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.game_width = game_width
        self.game_height = game_height

    def draw(self, surface):
        # Create planet surface and draw onto main surface
        planet_surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(planet_surf, self.color, (self.radius, self.radius), self.radius)
        surface.blit(planet_surf, (self.x - self.radius, self.y - self.radius))
    
    def planet_grow(self, mass):
        self.mass += mass
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


