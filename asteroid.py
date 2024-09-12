from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white',(self.x, self.y), self.radius, 2)
    
    def update(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += 100 * dt