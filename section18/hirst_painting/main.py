import turtle as turtle_module
import random
from extract_rgb_from_image import extract_colors

# this operation takes a few seconds, could extract into a static value to save time
color_list = extract_colors()

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.penup()
turtle.hideturtle()

# define starting position
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)
turtle.speed('fastest')

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  turtle.dot(20, random.choice(color_list))
  turtle.forward(50)

  if dot_count % 10 == 0:
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()