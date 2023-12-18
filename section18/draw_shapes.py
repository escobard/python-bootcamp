# use turtle module to draw shapes
## https://docs.python.org/3/library/turtle.html#introduction
### draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
from turtle import Turtle, Screen
import random

arrow = Turtle()
arrow.shape('arrow')
arrow.color('black')

colors = ['GreenYellow', 'Chocolate', 'Gold', 'LightSeaGreen', 'SkyBlue', 'MediumBlue', 'DodgerBlue', 'Brown', 'LightSkyBlue']

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    arrow.forward(100)
    arrow.right(angle)

# runs loop from numbers 3-10
## starts the loop at triangle (3 sides), to square (4 sides) and so on
for shape_side_n in range (3, 11):
  arrow.color(random.choice(colors))
  draw_shape(shape_side_n)