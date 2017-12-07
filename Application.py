import arcade
import Player
import Token
import random
screenWidth = 800
screenHeight = 600
recWidth = 50
recHeight = 50
moveSpeed = 5
fMoveSpeed = 2


class application(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard Control")
        self.player = None
        self.follower = None
        self.token = None
        self.left_down = False
        self.score = 0

    def setup(self):

        width = recWidth
        height = recHeight
        x = screenWidth // 2
        y = screenHeight // 2
        tokenH = 9
        tokenW = 9
        angle = 0
        color = arcade.color.WHITE
        fcolor = arcade.color.RED
        tcolor = arcade.color.YELLOW
        self.player = Player.player(x, y, width, height, angle, color)
        self.follower = Player.player(x + 20, y + 20, width, height, angle, fcolor)
        self.token = Token.token(tokenW, tokenH, tcolor, angle)

        self.left_down = False

    def update(self, dt):
        self.player.move()
        self.follower.move()

        # Makes follower follow the player
        # TODO stop the follower from shaking
        if self.follower.x < self.player.x:
            self.follower.delta_x = fMoveSpeed
        if self.follower.x > self.player.x:
            self.follower.delta_x = -fMoveSpeed
        if self.follower.y < self.player.y:
            self.follower.delta_y = fMoveSpeed
        if self.follower.y > self.player.y:
            self.follower.delta_y = -fMoveSpeed

        if (self.player.x < (self.token.x + 25) and self.player.x > (self.token.x - 25)
                and self.player.y < (self.token.y + 25) and self.player.y > (self.token.y - 25)):
            self.token.resPos()
            self.score += 1

        #arcade.draw_text("Points: " + str(self.score), 50, 550, arcade.color.WHITE, 12)


    def on_draw(self):
        arcade.start_render()
        self.token.draw()
        self.player.draw()
        self.follower.draw()
        arcade.draw_text("Points: " + str(self.score), 50, 550, arcade.color.WHITE, 12)

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
