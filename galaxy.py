import random
from planet import Planet


class Galaxy:
    def __init__(self, num_planets, width, height):
        self.num_planets = num_planets
        self.width = width
        self.height = height
        self.planets = []
        self.generate()

    def generate(self):
        # Create planet objects
        self.planets = []
        for i in range(self.num_planets):
            self.create_planet()
            
    def create_planet(self):
        mass = random.randint(50, 200)
        radius = mass // 5  # proportionate to mass
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(radius, self.width - radius)
        y = random.randint(radius, self.height - radius)
        planet = Planet(x, y, radius, mass, color, self.width, self.height)
        self.add_planet(planet)

    def add_planet(self, planet):
        self.planets.append(planet)
        self.num_planets = len(self.planets)

    def remove_planet(self, planet):
        self.planets.remove(planet)
        self.num_planets = len(self.planets)

    def clear(self):
        self.planets = []
        self.num_planets = 0