from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(-250, 270)
        self.write(f"SCORE:{self.score}", align='left', font=('Arial', 12, 'normal'))

    def increment_score(self):
        self.goto(-250, 270)
        self.score += 1
        self.clear()
        self.write(f"SCORE:{self.score}", align='left', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align='center', font=('Arial', 12, 'normal'))
        
    def increment_level(self, bricks_left):
        self.goto(100, 270)
        self.level += 1
        self.clear()
        self.write(f"LEVEL:{self.level}", align='left', font=('Arial', 12, 'normal'))