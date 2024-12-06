import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
            
        new_radius = self.radius - ASTEROID_MIN_RADIUS
            
        vector_one = self.velocity.rotate(random_angle) * 1.2
        vector_two = self.velocity.rotate(-random_angle) * 1.2
            
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one
            
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = vector_two
            
        return asteroid_one, asteroid_two
            