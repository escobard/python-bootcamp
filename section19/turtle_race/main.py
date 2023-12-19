import random
from turtle import Turtle, Screen

is_race_on = False
## can pass in the shape as an argument to the class init - nice!
screen = Screen()

# allows for the creation of a window with specific pixel sizes
## for readability, it is recommended to write the function argument names when invoking a function
screen.setup(height=400, width=500)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_position = -100

## store all turtles in an array to refer to each turtle later on
all_turtles = []

for color in colors:
  turtle = Turtle(shape='turtle')
  turtle.color(color)
  turtle.penup()
  ## move turtle to the specified location on the screen
  turtle.goto(x=-230, y=starting_position)
  starting_position += 30
  ## append turtle to array
  all_turtles.append(turtle)

if user_bet:
  is_race_on = True

while is_race_on:

  ## loop through turtles array to control each turtle
  for turtle in all_turtles:
    ## control win conditions if turtle reaches end of the screen
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      print(f"The winning color is: {winning_color}")
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner")

    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()