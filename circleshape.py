import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: object):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, circle: object):
        distance = pygame.math.Vector2.distance_to(self.position, circle.position)
        if self.radius + circle.radius > distance:
            return True
        else:
            return False
