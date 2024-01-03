import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()


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

  # detect collision with food
  if snake.head.distance(food) < 20:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # detect collision with wall
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    ## end the game if snake hits the wall
    game_is_on = False
    scoreboard.game_over()

  # detect collision with tail
  for segment in snake.segments:
    ## ignore collision rules for head of snake
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()