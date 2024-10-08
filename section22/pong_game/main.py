import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  #Detect collision with top/bottom wall
  ## ignores left/right wall, as that will reset the game
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # detect collision with paddles
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # detect right paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.left_point()

  # detect if left paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.right_point()


screen.exitonclick()