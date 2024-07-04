import time
from turtle import Turtle
import display
from projectile import Projectile

class Shooter(Turtle):
    def __init__(self, position, shoot_callback, display):
        super().__init__()
        self.custom_shape = "shooter.gif"
        self.shape(self.custom_shape)
        self.color("white")
        self.penup()
        self.goto(position)
        self.shoot_callback = shoot_callback
        self.lives = 3
        self.display = display
        self.display.set_lives(self.lives)
        self.last_shot_time = 0
        self.shoot_cooldown = 1.6

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            projectile = Projectile(self.position(), "shooter")
            self.shoot_callback(projectile)
            self.last_shot_time = current_time

    def reset_position(self):
        self.goto(0, -350)

    def lose_life(self):
        self.lives -= 1
        self.display.set_lives(self.lives)
        if self.lives == 0:
            self.game_over()

    def game_over(self):
        self.hideturtle()
        display.display_message(self, "GAME OVER")

