import pygame
from constants import LINE_WIDTH, HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_RADIUS

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
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
    def __init__(self, x, y):
        super().__init__(x, y, HOUSE_RADIUS)
        self.capacity = 4
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, "brown", (self.x, self.y, HOUSE_WIDTH, HOUSE_HEIGHT))

    def update(self, dt):
        self.position


class Tree(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, HOUSE_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius - right
        c = self.position + forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle())

    def cut_down(self):
        self.kill()