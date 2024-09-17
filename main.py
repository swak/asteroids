import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    # Initialize Pygame
    pygame.init()
    print("Starting asteroids!")

    # Set up the game window
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spaceship Game")

    # Create clock object to control frame rate
    clock = pygame.time.Clock()

    # Create two groups: updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign the groups to containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    #Initialize dt (delta time)
    dt = 0

    # Create a player object in the center of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Game logic here
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # Fill the screen with black
        screen.fill((0,0,0))

        # Draw the player (spaceship)
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and get the time since last frame
        dt = clock.tick(60) / 1000 # Convert milliseconds to seconds

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
