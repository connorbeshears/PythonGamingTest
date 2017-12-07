import arcade

sHeight = 800
sWidth = 600
recWidth = 50
recHeight = 50
moveSpeed = 5

class Player:

    def __init__(self, x, y, width, height, angle, color):
        self.x = x
        self.y = y

        self.delta_x = 0
        self.delta_y = 0

        self.width = width
        self.height = height
        self.angle = angle
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width,
                                     self.height, self.color, self.angle)

    def move(self):
        self.x += self.delta_x

        if self.x < recWidth // 2:
            self.x = recWidth // 2
        #TODO: Finish this here
