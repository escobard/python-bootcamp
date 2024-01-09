import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States game')

# load new image as turtle shape
image = 'blank_states_img.gif'
screen.setup(width=725, height=461)
screen.addshape(image)
turtle.shape(image)


correct_guesses = []
# add an input to the turtle screen to get user answer

answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name")
answer_to_lower = answer_state.lower()
answer = answer_to_lower.capitalize()

data = pandas.read_csv('50_states.csv')
check_guess = data[data.state == answer]

print(check_guess)

screen.exitonclick()