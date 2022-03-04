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
        # Degrees to radians
        self.angle = random.randint(-60, 60)
        while -5 < self.angle < 5:
            self.angle = random.randint(-60, 60)
        self.angle = (self.angle * 0.01745)
        if self.angle >= 0:
            self.dir_x = -1
        else:
            self.dir_x = 1
        self.dir_y = 1
        self.setheading(self.angle)
        # direction 1=up, -1=down
        self.direction = 1
        self.speed(10)

    def move_ball(self):
        self.detect_collision_with_wall()
        # count new_x based on tangens fun
        new_x = self.xcor() + (math.tan(abs(self.angle)) * 5 * self.dir_x)
        new_y = self.ycor() + (5 * self.dir_y)
        self.goto(new_x, new_y)

    def detect_collision_with_wall(self):
        current_y_pos = self.ycor()
        current_x_pos = self.xcor()
        # X axis right wall collision
        if self.distance(300, current_y_pos) < 20:
            if self.direction == 1:
                self.dir_y = 1
            else:
                self.dir_y = -1
            self.dir_x = -1
        # X axis left wall collision
        elif self.distance(-300, current_y_pos) < 20:
            if self.direction == 1:
                self.dir_y = 1
            else:
                self.dir_y = -1
            self.dir_x = 1
        # Y axis right up collision
        elif self.distance(current_x_pos, 300) < 20:
            self.dir_y = -1
            self.direction = -1
        return self.dir_x, self.dir_y

    def detect_collision_with_player(self):
        self.direction = 1
        self.dir_y = 1
        
    def detect_collision_with_brick(self):
        self.direction *= -1
        self.dir_y *= -1