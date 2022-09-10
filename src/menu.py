import arcade

class MenuView(arcade.View):
    """The main menu."""

    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        self.clear()

        center_x = self.WIDTH / 2
        center_y = self.HEIGHT / 2
        title_size = self.WIDTH / 4
        button_size = self.WIDTH / 6

        arcade.draw_text("Snake Pong", center_x, center_y, arcade.color.BLACK, font_size=title_size, anchor_x="center")

        