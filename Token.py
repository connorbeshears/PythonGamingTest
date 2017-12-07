import arcade


class token:

    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.angle = angle

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)
