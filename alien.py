import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

