from turtle import Screen, Turtle
import time

screen = Screen()
# using named arguments to improve readability
screen.setup(width=600, height=600)
screen.bgcolor('black')
# add a title to application screen
screen.title('Snake Game')
# turns off automatic transitions for animations
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
  new_segment = Turtle('square')
  new_segment.color('white')
  new_segment.penup()
  new_segment.goto(position)
  segments.append(new_segment)



game_is_on = True
while game_is_on:
  # tells the screen to update
  ## only updates the screen after all squares have been rendered / finished moving, useful!
  screen.update()
  time.sleep(0.1)
  # run a loop to move each individual segment, going backwards through the segments
  ## for seg_num in range(start=2, stop=0, step=-1):
  for seg_num in range(len(segments) - 1, 0, -1):
    # grabs x coordinates from next segment
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    # sets coordinates of segment to coordinates of next segment
    segments[seg_num].goto(new_x, new_y)

  # move first segment forward after all other segments have been moved
  segments[0].forward(20)

screen.exitonclick()