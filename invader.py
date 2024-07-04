from turtle import Turtle

class SpaceInvader(Turtle):
    def __init__(self, position, shape_image):
        super().__init__()
        self.shape(shape_image)
        self.penup()
        self.goto(position)
        self.speed("fastest")
        self.is_alive = True

    def move(self, dx, dy):
        if self.is_alive:
            new_x = self.xcor() + dx
            new_y = self.ycor() + dy
            self.goto(new_x, new_y)

    def destroy(self):
        self.hideturtle()
        self.is_alive = False
