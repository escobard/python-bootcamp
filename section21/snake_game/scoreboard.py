from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    ## Turtle method to write on the screen
    self.hideturtle()
    self.color('white')
    self.penup()
    self.goto(0, 260)
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    ## clears the rendered turtles before updating the score
    self.clear()
    self.update_scoreboard()

  def game_over(self):
    self.goto(0,0)
    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
