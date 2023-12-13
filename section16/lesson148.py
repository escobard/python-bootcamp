# basic class / object declaration in python
## globally available module, creates a GUI
### https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

# create class instance/object by assigning variable
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('coral')

my_screen = Screen()
print(my_screen.canvheight)
timmy.forward(100)

# call a method on the class
my_screen.exitonclick()