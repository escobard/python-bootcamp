# keyboard event listeners in python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
  tim.forward(10)


## tells the library to listen for events
screen.listen()
## listens for the specific onkey event
### passes move_forward function without brackets to avoid invoking the function
#### passing a function as an argument to another function is known as a higher order function in python
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()