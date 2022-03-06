from turtle import Screen
from player import Bat
from bricks import Brick, BricksWall
from ball import Ball
from scoreboard import ScoreBoard
from level import Level
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
scoreboard = ScoreBoard()
level = Level()


screen.listen()
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")

while not game_over:

    screen.update()
    time.sleep(0.000001)
    ball.move_ball(level.level)
    if ball.distance(player) < 35 and ball.ycor() < -265:
        ball.collision_with_player()
    for brick in board.bricks_wall:
        if ball.distance(brick) < 35:
            ball.collision_with_brick()
            board.destroy_brick(brick)
            scoreboard.increment_score()
            break
    if ball.ycor() < -280:
        game_over = True
        scoreboard.game_over()
    if len(board.bricks_wall) == 0:
        level.increment_level()
        ball.restart_level()
        board.create_board()

screen.exitonclick()