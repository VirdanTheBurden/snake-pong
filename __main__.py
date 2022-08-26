# TODO: field initialization, apple seeding, paddle spawning, etc.

import arcade

# Constants, do not touch
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TITLE = "Snake Pong"

class SnakePong(arcade.Window):
    """Main application class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.GRAY)
    
    def setup(self):
        """Draw paddle and snake."""
        pass

    def on_draw(self):
        self.clear()

def main():
    window = SnakePong()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()