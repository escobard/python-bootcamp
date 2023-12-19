from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(3)


def move_forwards():
  tim.forward(10)
  tim.position()

def move_backwards():
  tim.backward(10)

def move_left():
  tim.left(45)
  tim.forward(10)

def move_right():
  tim.right(45)
  tim.forward(10)

def clear_screen():
  tim.reset()

screen.listen()

screen.onkey(key="Right", fun=move_forwards)
screen.onkey(key="Left", fun=move_backwards)
screen.onkey(key="Up", fun=move_left)
screen.onkey(key="Down", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()