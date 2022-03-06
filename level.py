from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(100, 270)
        self.write(f"LEVEL:{self.level}", align='left', font=('Arial', 12, 'normal'))

    def increment_level(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL:{self.level}", align='left', font=('Arial', 12, 'normal'))