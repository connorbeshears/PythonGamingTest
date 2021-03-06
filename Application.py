import arcade
import math
import Player
import Token
import Turret
import Bullet
import random
screenWidth = 800
screenHeight = 600
recWidth = 25
recHeight = 25
moveSpeed = 5
fMoveSpeed = 2
bulletSpeed = 9
bulletDamage = 1
playerHealth = 10


class application(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard Control")
        self.player = None
        self.turret = None
        self.token = None
        self.bullet = None
        self.left_down = False
        self.dead = False
        self.score = 0
        self.frameCount = 0
        self.bulletList = []

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
        self.player = Player.player(x, y, width, height, angle, color, playerHealth)
        self.token = Token.token(tokenW, tokenH, tcolor, angle)
        self.turret = Turret.Turret(10, 300, 18, 8, fcolor, angle)
        self.bullet = Bullet.Bullet(10, 300, 0)

        self.left_down = False

    def update(self, dt):
        if(self.dead == False):
            self.player.move()
            self.frameCount += 1

            # Makes turret face the player
            startX = self.turret.x
            startY = self.turret.y
            tarX = self.player.x
            tarY = self.player.y

            diffX = tarX - startX
            diffY = tarY - startY

            angle = math.atan2(diffY, diffX)
            self.turret.angle = math.degrees(angle)

            if self.frameCount % 20 == 0:
                self.bullet = Bullet.Bullet(startX, startY, self.turret.angle)
                self.bullet.deltaX = math.cos(angle) * bulletSpeed
                self.bullet.deltaY = math.sin(angle) * bulletSpeed
                self.bulletList.append(self.bullet)


            if (self.player.x < (self.token.x + 25) and self.player.x > (self.token.x - 25)
                    and self.player.y < (self.token.y + 25) and self.player.y > (self.token.y - 25)):
                self.token.resPos()
                self.score += 1

            if(self.player.health <= 0):
                self.dead = True


    def on_draw(self):
        arcade.start_render()
        self.token.draw()
        self.player.draw()
        self.turret.draw()
        for bullet in self.bulletList:
            bullet.move()
            bullet.draw()
            if bullet.x > screenWidth:
                self.bulletList.remove(bullet)
            if bullet.y > screenHeight:
                self.bulletList.remove(bullet)

            if bullet.x >= self.player.x -10 and bullet.x <= self.player.x + 10 and \
                            bullet.y <= self.player.y + 10 and bullet.y >= self.player.y - 10:
                self.bulletList.remove(bullet)
                self.player.health -= bulletDamage

        arcade.draw_text("Points: " + str(self.score), 10, 575, arcade.color.WHITE, 12)
        arcade.draw_text("Health: " + str(self.player.health), 700, 575, arcade.color.WHITE, 12)

        if(self.dead == True):
            arcade.draw_text("Game over", 300, 300, arcade.color.WHITE, 34)

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
