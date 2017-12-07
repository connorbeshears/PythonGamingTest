import arcade
import random

class token:

    def __init__(self, width, height, color, angle):
        self.x = random.randint(1, 801)
        self.y = random.randint(1, 601)
        self.height = height
        self.width = width
        self.color = color
        self.angle = angle

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

    def resPos(self):
        self.x = random.randint(1, 801)
        self.y = random.randint(1, 601)

