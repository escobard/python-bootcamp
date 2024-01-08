from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    # assign the head of the snake to a class variable
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      # grabs x coordinates from next segment
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      # sets coordinates of segment to coordinates of next segment
      self.segments[seg_num].goto(new_x, new_y)

    # move first segment forward after all other segments have been moved
    self.segments[0].forward(MOVE_DISTANCE)

  def add_segment(self, position):
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def reset(self):
    ## makes dead snake disappear off the screen
    for seg in self.segments:
      seg.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]

  ## adds a new segment to the snake
  def extend(self):
    ## add segment to the last segment in the list
    self.add_segment(self.segments[-1].position())


  def up(self):
    # only allows for turn if heading is not heading down
    ## checks the heading of the lead turtle to determine if snake can turn up or down
    if self.head.heading() != DOWN:
      ## turn the snake's head up / 90 degrees
      self.head.setheading(UP)

  def down(self):
    ## turn the snake's head up / 90 degrees
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      ## turn the snake's head up / 90 degrees
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      ## turn the snake's head up / 90 degrees
      self.head.setheading(RIGHT)
