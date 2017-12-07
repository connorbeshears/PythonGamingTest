import arcade
import Player
screenWidth = 800
screenHeight = 600
recWidth = 50
recHeight = 50
moveSpeed = 5

class application(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard Control")
        self.player = None
        self.left_down = False

    def setup(self):
        width = recWidth
        height = recHeight
        x = screenWidth // 2
        y = screenHeight // 2
        angle = 0
        color = arcade.color.WHITE
        self.player = Player.player(x, y, width, height, angle, color)
        self.left_down = False

    def update(self, dt):
        self.player.move()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.delta_y = moveSpeed
        elif key == arcade.key.DOWN:
            self.player.delta_y = -moveSpeed
        elif key == arcade.key.LEFT:
            self.player.delta_x = -moveSpeed
        elif key == arcade.key.RIGHT:
            self.player.delta_x = moveSpeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.delta_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.delta_x = 0
