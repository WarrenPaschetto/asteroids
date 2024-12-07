import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, image_path="images/spaceship.png"):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0
    
    # Load the player image and set its initial state
        self.image = pygame.image.load(image_path).convert_alpha()
        self.original_image = self.image  # Keep the original image for rotation
        self.rect = self.image.get_rect(center=(x, y))
    
    def draw(self, screen):
        # Rotate the image and update its position
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)  # Negate rotation for correct orientation
        self.rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_image, self.rect.topleft)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(Shot)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, bullet_class):
        if self.timer > 0:
            return
        else:
            bullet_class(self.position.x, self.position.y, SHOT_RADIUS, pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
            self.timer = PLAYER_SHOOT_COOLDOWN
        