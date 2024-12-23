import pygame

class Button:
    """A class to build buttons for the game"""

    def __init__(self, game, msg):
        """Initialize button attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimension and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Add text to button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered text"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button and message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
