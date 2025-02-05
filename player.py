import pygame
from circleshape import *
from constants import *
from shot import Shot

# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        forward = forward * PLAYER_SHOT_SPEED
        Shot(self.position.x, self.position.y, SHOT_RADIUS, forward)

    attack_cd = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            if self.attack_cd < 0: 
                self.shoot()
                self.attack_cd = PLAYER_SHOOT_COOLDOWN
            else: self.attack_cd -= dt
