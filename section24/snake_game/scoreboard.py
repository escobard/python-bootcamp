from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.read_score()
    self.hideturtle()
    self.color('white')
    self.penup()
    self.goto(0, 260)
    self.update_scoreboard()

  def read_score(self):
    with open('data.txt') as file:
      return int(file.read())

  def write_score(self, score: int = 0):
    with open('data.txt', mode='w') as file:
      return file.write(str(score))

  def update_scoreboard(self):
    self.clear()
    ## Turtle method to write on the screen
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    ## clears the rendered turtles before updating the score
    self.update_scoreboard()

  # def game_over(self):
  #   self.goto(0,0)
  #   self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.write_score(self.score)
      self.high_score = self.read_score()
    self.score = 0
    self.update_scoreboard()