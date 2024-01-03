from turtle import Screen, Turtle

screen = Screen()
# using named arguments to improve readability
screen.setup(width=600, height=600)
screen.bgcolor('black')
# add a title to application screen
screen.title('Snake Game')


screen.exitonclick()