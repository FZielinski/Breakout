from turtle import Turtle


class Bat(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.penup()
        self.hideturtle()
        self.goto(0, -280)
        self.showturtle()
        
    def move_left(self):
        if self.xcor() > -250:
            self.goto(self.xcor()-50, self.ycor())
        
    def move_right(self):
        if self.xcor() < 250:
            self.goto(self.xcor()+50, self.ycor())
