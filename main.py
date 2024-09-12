import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for u in updateable:
            u.update(dt)
        
        screen.fill('black')

        for d in drawable:
            d.draw(screen)
        
        
        pygame.display.flip()
        # Limit framerate to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()