import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            pygame.sprite.Sprite.__init__(self, self.containers)
        else:
            pygame.sprite.Sprite.__init__(self)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def detect_collision(self, circle):
        distance = self.position.distance_to(circle.position)
        if distance <= self.radius + circle.radius: return True
        else: return False
        