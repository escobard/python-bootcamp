import random
from turtle import Turtle

## inherits from the turtle class
class Food(Turtle):

  def __init__(self):
    ## inherits the constructors from the parent class
    super().__init__()

    ### all inherited methods from the turtle superclass
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color('blue')
    self.speed('fastest')
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)

    ### renders food at the specified coordinates
    self.goto(random_x, random_y)