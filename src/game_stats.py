class GameStats:
    # Track statistics for Alien Invasion
    
    def __init__(self, ai_game):
        # Initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Setting Alien Invasion in the bottom of the screen
        self.game_active = True
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        