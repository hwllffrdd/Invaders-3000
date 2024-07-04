from turtle import Turtle

class Display(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.lives = 3
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="left", font=("Arial", 16, "normal"))

    def set_lives(self, lives):
        self.lives = lives
        self.update_display()


def display_message(message, position=(0, 0)):
        pen = Turtle()
        pen.hideturtle()
        pen.penup()
        pen.color("white")
        pen.goto(position)
        pen.write(message, align="center", font=("Arial", 36, "normal"))

