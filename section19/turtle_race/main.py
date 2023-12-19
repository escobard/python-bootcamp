from turtle import Turtle, Screen

## can pass in the shape as an argument to the class init - nice!
screen = Screen()

# allows for the creation of a window with specific pixel sizes
## for readability, it is recommended to write the function argument names when invoking a function
screen.setup(height=400, width=500)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_position = -100

for color in colors:
  turtle = Turtle(shape='turtle')
  turtle.color(color)
  turtle.penup()
  ## move turtle to the specified location on the screen
  turtle.goto(x=-230, y=starting_position)
  starting_position += 30


screen.exitonclick()