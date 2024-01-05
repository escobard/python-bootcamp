import time
from turtle import Screen

from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

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
  ## ignores left/right wall, as that will score points for the opposite paddle
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # detect collision with paddles
  if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() > -340:
    ball.bounce_x()

screen.exitonclick()