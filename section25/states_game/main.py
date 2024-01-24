import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States game')

# load new image as turtle shape
image = 'blank_states_img.gif'
screen.setup(width=725, height=461)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []
# add an input to the turtle screen to get user answer

game_is_on = True

def write_state(x, y, state_name):
  state = turtle.Turtle()
  state.hideturtle()
  state.color('black')
  state.penup()
  state.goto(x, y)
  state.write(state_name)

while game_is_on:
  answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states correct', prompt="Guess a state's name")
  answer_to_lower = answer_state.lower()
  answer = answer_to_lower.capitalize()

  check_guess = data[data.state == answer]
  print(check_guess.to_dict())
  if answer == 'Exit':
    # no pandas function to help you parse data back into a useful format, should be done with python directly
    missing_states = []
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)

    # pandas converts each index from a list to a column as a key/value pair - awesome!
    dataframe = pandas.DataFrame(missing_states)

    # convert existing or new data frames to csv
    dataframe.to_csv('missing_states.csv')
    print(missing_states)
    break
  if answer in all_states:
    guessed_states.append(answer)
    # big gotcha with pandas - returns a string with useless values for a single value
    ## apparently, it has to be converted to the expected type and the right value will be returned
    ### there is a type error when converting pandas variables to strings directly, instead use series.property.iloc[0] to avoid warnings
    write_state(int(check_guess.x.iloc[0]), int(check_guess.y.iloc[0]), answer)
    print('correct!')

  # print(check_guess)

screen.exitonclick()
