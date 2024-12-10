import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the player's ship"""

    def __init__(self, game):
        """Initialize the ship on the screen"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the center of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store horizontal position in a float
        self.x = float(self.rect.x)
        
        # Movement flag; no movement by default
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)


    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship to the middle of the screen on getting hit"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
