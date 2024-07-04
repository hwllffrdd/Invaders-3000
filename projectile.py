from turtle import Turtle

class Projectile(Turtle):
    def __init__(self, position, owner):
        super().__init__()
        self.shape("square")
        self.color("red" if owner == "shooter" else "blue")
        self.shapesize(stretch_wid=1, stretch_len=0.2)
        self.penup()
        self.goto(position)
        self.owner = owner


    def move(self):
        new_y = self.ycor() + 3 if self.owner == "shooter" else self.ycor() - 3
        self.goto(self.xcor(), new_y)

    def check_collision(self, obstacle):
        return obstacle.check_collision(self)