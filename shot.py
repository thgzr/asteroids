import pygame
from circleshape import *
from constants import *
from asteroid import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.color = (255, 255, 255)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt