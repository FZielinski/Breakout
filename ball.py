import random
from turtle import Turtle
import math


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.pencolor("white")
        self.fillcolor("green")
        self.penup()
        self.hideturtle()
        self.goto(0, -262)
        self.showturtle()
        self.dir_x = 1
        self.dir_y = 1
        self.angle = random.randint(-30, 30)
        print(self.angle)
        self.setheading(self.angle)
        # direction 1=up, 0=down
        self.direction = 1

    def move_ball(self):
        self.detect_collision_with_wall()
        # count new_x based on tangens fun
        new_x = self.xcor() + (math.tan(self.angle) * 5 * self.dir_x)
        new_y = self.ycor() + (5 * self.dir_y)
        self.goto(new_x, new_y)

    def detect_collision_with_wall(self):
        current_y_pos = self.ycor()
        current_x_pos = self.xcor()
        print(self.distance(300, current_y_pos))
        # X axis right wall collision
        if self.distance(300, current_y_pos) < 20:
            if self.direction == 1:
                self.dir_x = -1
                self.dir_y = 1
            else:
                self.dir_x = -1
                self.dir_y = -1
        # X axis left wall collision
        elif self.distance(-300, current_y_pos) < 20:
            if self.direction == 1:
                self.dir_x = 1
                self.dir_y = 1
            else:
                self.dir_x = 1
                self.dir_y = -1
        # Y axis right up collision
        elif self.distance(current_x_pos, 300) < 20:
            self.dir_x = -1
            self.dir_y = -1
            self.direction = 0
        return self.dir_x, self.dir_y
    