# make the turtle walk randomly and each line should have a random color, use a thick line and speed up the turtle
## for more information on the applications of the random walk algorithm - https://en.wikipedia.org/wiki/Random_walk - pretty fascinating stuff
from turtle import Turtle, Screen
import random
from colors import colors

turtle = Turtle()
turtle.shape('circle')
turtle.color('black')
turtle.speed('fast')
turtle.pensize(20)


def turn_right(angle):
  return turtle.right(angle)


def turn_left(angle):
  return turtle.left(angle)


direction = [turn_left, turn_right]

for _ in range(1, 101):
  turtle.forward(100)
  turtle.color(random.choice(colors))
  random_direction = random.choice(direction)
  random_direction(90)
