from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')

for _ in range(15):
  tim.forward(20)
  tim.penup()
  tim.forward(20)
  tim.pendown()

screen = Screen()
screen.exitonclick()