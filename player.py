import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    containers = None # This will be assigned in main.py to the groups

    def __init__(self, x, y):
        # Initialize the CircleShape with position and radius
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # Players rotation angle

        # Add the player instance to the sprite groups
        if Player.containers:
            for group in Player.containers:
                group.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt, direction):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)

        if keys[pygame.K_d]:
            self.rotate(dt, 1)

        if keys[pygame.K_w]:
            self.move(dt, 1)

        if keys[pygame.K_s]:
            self.move(dt, -1)
