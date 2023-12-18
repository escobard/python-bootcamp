# make the turtle walk randomly and each line should have a random color, use a thick line and speed up the turtle
## for more information on the applications of the random walk algorithm - https://en.wikipedia.org/wiki/Random_walk - pretty fascinating stuff
from turtle import Turtle, Screen
import random
from colors import colors

turtle = Turtle()
turtle.shape('circle')
turtle.color('black')
turtle.speed('fastest')
turtle.pensize(15)


direction = [0, 90, 180, 270]

for _ in range(1, 201):
  turtle.forward(50)
  turtle.color(random.choice(colors))
  turtle.setheading(random.choice(direction))
