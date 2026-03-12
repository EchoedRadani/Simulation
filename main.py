import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from classes import House, Tree


def main():
    print("Starting simulation, running pygame version:", pygame.version.ver)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    print("Spawning trees...")
    trees = []
    for _ in range(50):
        ran_x = random.randint(5, SCREEN_WIDTH - 5)
        ran_y = random.randint(5, SCREEN_HEIGHT - 5)
        trees.append(Tree(ran_x, ran_y))

    House.containers = (updatable, drawable)
    Tree.containers = (updatable, drawable)

    house = House(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # tree = Tree(1000, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for items in drawable:
            items.draw(screen)

        for tree in trees:
            tree.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
