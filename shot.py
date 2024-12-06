import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(velocity)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        