import time
from turtle import Screen

from food import Food
from snake import Snake

screen = Screen()
# using named arguments to improve readability
screen.setup(width=600, height=600)
screen.bgcolor('black')
# add a title to application screen
screen.title('Snake Game')
# turns off automatic transitions for animations
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
  # tells the screen to update
  ## only updates the screen after all squares have been rendered / finished moving, useful!
  screen.update()
  time.sleep(0.1)
  snake.move()

screen.exitonclick()