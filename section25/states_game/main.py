import turtle

screen = turtle.Screen()
screen.title('U.S. States game')

# load new image as turtle shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()