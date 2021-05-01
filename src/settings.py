class Settings:
    # Class to store all settings for the game

    def __init__(self):
        # Initialize the game's settings
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 5
