from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    # assign the head of the snake to a class variable
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_segment = Turtle('square')
      new_segment.color('white')
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      # grabs x coordinates from next segment
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      # sets coordinates of segment to coordinates of next segment
      self.segments[seg_num].goto(new_x, new_y)

    # move first segment forward after all other segments have been moved
    self.segments[0].forward(MOVE_DISTANCE)

  def up(self):
    ## turn the snake's head up / 90 degrees
    self.head.setheading(90)

  def down(self):
    ## turn the snake's head up / 90 degrees
    self.head.setheading(270)

  def left(self):
    ## turn the snake's head up / 90 degrees
    self.head.setheading(180)

  def right(self):
    ## turn the snake's head up / 90 degrees
    self.head.setheading(0)