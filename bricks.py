import random
from turtle import Turtle
from random import choice,randint


class Brick(Turtle):
    def __init__(self, start_x, start_y):
        colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']
        super().__init__()
        self.shapesize(1, 2.5)
        self.hideturtle()
        self.shape("square")
        self.pencolor("white")
        self.fillcolor(random.choice(colors))
        self.penup()
        self.speed(0)
        self.goto(start_x, start_y)
        self.showturtle()


class BricksWall(Brick):
    def __init__(self):
        self.bricks_wall = []
        self.x_start = -250
        self.y_start = 250

    def create_board(self):
        for j in range(1):
            brick = Brick(self.x_start, self.y_start)
            self.bricks_wall.append(brick)
            for i in range(1):
                brick = Brick(self.bricks_wall[len(self.bricks_wall) - 1].xcor() + 55,
                              self.bricks_wall[len(self.bricks_wall) - 1].ycor())
                self.bricks_wall.append(brick)
            self.y_start -= 30
    
    def destroy_brick(self, brick):
        self.bricks_wall.remove(brick)
        brick.hideturtle()
        
        