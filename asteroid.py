import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, image_path="images/asteroid.png"):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)
        self.image_path = image_path
        
        # Load the asteroid image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (radius * 2, radius * 2))  # Scale to radius
        self.rect = self.image.get_rect(center=(x, y))
    
    def draw(self, screen):
        # Update rect position based on the asteroid's current position
        self.rect.center = (int(self.position.x), int(self.position.y))
        screen.blit(self.image, self.rect.topleft)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Adjust velocities for the new smaller asteroids
        vector_one = self.velocity.rotate(random_angle) * 1.2
        vector_two = self.velocity.rotate(-random_angle) * 1.2

        # Create new asteroids with the same image
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius, self.image_path)
        asteroid_one.velocity = vector_one

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius, self.image_path)
        asteroid_two.velocity = vector_two

        return asteroid_one, asteroid_two
