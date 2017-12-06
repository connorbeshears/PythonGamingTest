import arcade
import math


#set up some constants here
screenWidth = 800
screenHeight = 600
xCenter = screenWidth // 2
yCenter = screenHeight // 2
radiansFrame = 0.02
sweepLength = 250

def onRadarDraw(deltaTime):

    #Move Angle
    onRadarDraw.angle += radiansFrame

    #End point for line
    x = sweepLength * math.sin(onRadarDraw.angle) + xCenter
    y = sweepLength * math.cos(onRadarDraw.angle) + yCenter

    arcade.start_render()
    arcade.draw_line(xCenter, yCenter, x, y, arcade.color.AMETHYST, 4)
    arcade.draw_circle_outline(xCenter, yCenter, sweepLength, arcade.color.RED, 10)


onRadarDraw.angle = 0

arcade.open_window(screenWidth, screenHeight, "Radar Thing")
arcade.set_background_color(arcade.color.BLACK)

arcade.schedule(onRadarDraw, 1 / 80)


def drawBoxCircles():
    colSpace = 10
    rowSpace = 10
    lMargin = 50
    bMargin = 50
    arcade.start_render()
    for row in range(10):
        for col in range(10):
            x = col * colSpace + lMargin
            y = row * rowSpace + bMargin
            arcade.draw_circle_filled(x, y, 5, arcade.color.BLUE)
    arcade.finish_render()


arcade.run()
