from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position: tuple[float, float]):
    super().__init__()
    self.starting_position: tuple[float, float] = position

    self.shape('square')
    self.color('white')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(self.starting_position)

  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)