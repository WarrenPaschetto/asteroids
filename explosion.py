import pygame

# Explosion Class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.images = [pygame.image.load(f"images/explosion{i}.png") for i in range(3)]  # Load animation frames
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 0.15 # Adjust as needed
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.index += 1
            if self.index < len(self.images):
                self.image = self.images[self.index]
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.kill()  # Remove the sprite when animation is complete
