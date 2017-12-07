import arcade
import Application


#set up some constants here
screenWidth = 800
screenHeight = 600
recWidth = 50
recHeight = 50
moveSpeed = 5


window = Application.application(screenWidth, screenHeight)
window.setup()
arcade.run()
