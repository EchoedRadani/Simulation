import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
        radius = self.radius + other.radius
        distance = self.position.distance_to(other.position)
        return distance <= radius


class Person(CircleShape):
    pass

    # def __init__(self):
    #     self.heath = 100
    #     self.hunger = 100
    #     self.lumberjack = False
    #     self.builder = False
    #     self.farmer = False
    #     self.has_home = False


class House(CircleShape):
    pass