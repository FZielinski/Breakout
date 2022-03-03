from turtle import Screen
from player import Bat
from bricks import Brick, BricksWall
from ball import Ball
import time

screen = Screen()
game_over = False

screen.setup(width=600, height=600)
screen.title("Breakout")
screen.bgcolor("black")

player = Bat()
board = BricksWall()
board.create_board()
ball = Ball()

screen.listen()
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")

while not game_over:
    time.sleep(0.02)
    ball.move_ball()
    screen.update()

screen.exitonclick()