from turtle import Turtle

class Paddle:
  def __init__(self, position: tuple[float, float]):
    self.starting_position: tuple[float, float] = position
    self.paddle = Turtle()
    self.paddle = Turtle()
    self.paddle.shape('square')
    self.paddle.color('white')
    self.paddle.shapesize(stretch_wid=5, stretch_len=1)
    self.paddle.penup()
    self.paddle.goto(self.starting_position)

  def go_up(self):
    new_y = self.paddle.ycor() + 20
    self.paddle.goto(self.paddle.xcor(), new_y)

  def go_down(self):
    new_y = self.paddle.ycor() - 20
    self.paddle.goto(self.paddle.xcor(), new_y)