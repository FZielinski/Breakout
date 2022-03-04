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

    screen.update()
    time.sleep(0.000001)
    ball.move_ball()
    if ball.distance(player) < 35 and ball.ycor() < -265:
        ball.detect_collision_with_player()
    for brick in board.bricks_wall:
        if ball.distance(brick) < 35:
            ball.detect_collision_with_brick()
            board.destroy_brick(brick)
            break

screen.exitonclick()