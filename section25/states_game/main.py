import turtle

screen = turtle.Screen()
screen.title('U.S. States game')

# load new image as turtle shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# add an input to the turtle screen to get user answer
answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name")
answer_to_lower = answer_state.lower()
answer = answer_to_lower.capitalize()

print(answer)

screen.exitonclick()