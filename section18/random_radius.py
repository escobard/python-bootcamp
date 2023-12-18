# make the turtle walk randomly and each line should have a random color, use a thick line and speed up the turtle
## for more information on the applications of the random walk algorithm - https://en.wikipedia.org/wiki/Random_walk - pretty fascinating stuff
from turtle import Turtle, Screen, colormode
import random
from colors import colors, random_color

turtle = Turtle()
colormode(255)
turtle.shape('arrow')
turtle.speed('fastest')

def draw_spirograph(size_of_gap):
  ## we know 360 is the full degree cicle, use difference between size of gap and 360 to determine how many times the loop should run for a full 360
  for _ in range(int(360 / size_of_gap)):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()