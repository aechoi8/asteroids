import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Clock

    clock = pygame.time.Clock()
    dt = 0

    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #set groups to containers for asteroids, player, asteroids field
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable, )
    
    #instantiate objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #inifinite while loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #clear screen
        screen.fill((0, 0, 0))
        #update method
        updatable.update(dt)

        #check for collisions after update
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
            
        #re-render player
        for sprite in drawable:
            sprite.draw(screen)

        #updates the display
        pygame.display.flip()

        #pauses the game loop 1/60th of second
        dt = clock.tick(60)
        dt = dt / 1000
    
if __name__ == "__main__":
    main()
