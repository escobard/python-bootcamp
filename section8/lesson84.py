# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# Write your code below this line 👇
# Define a function called paint_calc() so the code below works.   
import math
def paint_calc(height, width, cover):
  cans_rounded = 0
  number_of_cans= (height * width) / cover
  if number_of_cans < 2:
    cans_rounded = 2
  elif number_of_cans >= 2:
    cans_rounded = math.ceil(number_of_cans)
  print(f"You'll need {cans_rounded} cans of paint.")



# Write your code above this line 👆
# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)