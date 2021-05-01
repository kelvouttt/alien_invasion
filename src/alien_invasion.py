import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    # Class to manage game assets and behavior

    def __init__(self):
        # Initializing the game, and create game resources
        pygame.init()
        self.settings = Settings()
        # Setting the width and height (0, 0) and use pygame.FULLSCREEN to get the max width, height
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN 
        )
        # Getting the width and height using .get_rect() on the screen and assign it to variable in settings
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        # Starting the main loop for the game
        while True:
            # Function to watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
           
    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Key press trigger to move ship right    
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Detecting whether keypress is released 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        # Respond to the keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False

    def _update_screen(self):
        # Update image on scree, and flip to new screen
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # Make the game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


