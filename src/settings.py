class Settings:
    # Class to store all settings for the game

    def __init__(self):
        # Initialize the game's settings
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.0
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 100
        self.alien_speed = 0.7
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
