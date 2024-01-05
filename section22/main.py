from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


paddle = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle.go_up, 'Up')
screen.onkey(paddle.go_down, 'Down')
screen.onkey(paddle_2.go_up, 'W')
screen.onkey(paddle_2.go_down, 'D')

game_is_on = True
while game_is_on:
  screen.update()

screen.exitonclick()