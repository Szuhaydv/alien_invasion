class Settings:
    """A class to store all the game's settings"""
    
    def __init__(self):
        """Initialize the game's static settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Set the ship's speed
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How fast the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings which change throughout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 5.0
        self.alien_speed = 1.0

        # fleet direction of 1 represents right, 0 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings and alien points values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.score_scale)
