import arcade


class Bullet:

    def __init__(self, x, y, angle):
        self.x = x
        self.deltaX = 0
        self.deltaY = 0
        self.y = y
        self.height = 3
        self.width = 7
        self.color = arcade.color.ANDROID_GREEN
        self.angle = angle

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width,
                                     self.height, self.color, self.angle)


    def move(self):
        self.x += self.deltaX
        self.y += self.deltaY
