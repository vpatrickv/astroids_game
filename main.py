# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update sprites
        updatable.update(dt)

        for astroid in asteroids:
            if player.check_collision(astroid):
                print("Game over!")
                sys.exit()

        for astroid in asteroids:
            for shot in shots:
                if shot.check_collision(astroid):
                    shot.kill()
                    astroid.split()

        # update screen
        #pygame.Surface.fill(screen, (0, 0, 0))
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        #limit game to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()