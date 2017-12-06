import arcade

arcade.open_window(600, 600, "Hello World")
arcade.set_background_color(arcade.color.WHITE)
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
