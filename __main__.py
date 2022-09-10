# TODO: field initialization, apple seeding, paddle spawning, etc.

import arcade
from src.menu import MenuView

# Constants, do not touch
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Snake Pong"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()

if __name__ == "__main__":
    main()