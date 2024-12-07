import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion


def main():
    pygame.get_init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("images/space.png")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2    
   
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    Explosion.containers = (updatable, drawable)
    
    Shot.containers = (updatable, drawable, shots)
    
    running = True
    while running:
        #screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        explosions.update(dt)
        explosions.draw(screen)
        
        for obj in updatable: 
            obj.update(dt)
            
        for obj in drawable:    
            obj.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                running = False
                
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    explosion = Explosion(asteroid.position)
                    explosions.add(explosion)
                    asteroid.split()
                    bullet.kill()     
            
        dt = clock.tick(60) / 1000
        pygame.display.flip()
 

if __name__ == "__main__":
    main()