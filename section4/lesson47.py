# You are going to write a program that will mark a spot on a map with an X.
# Your job is to write a program that allows you to mark a square on the map using a letter-number system.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# grabs letter from string
horizontal = position[0].lower()
abc = ['a', 'b', 'c']
horizontal_coordinates = abc.index(horizontal)
# grabs number from string
vertical = int(position[1]) - 1

# sets original coordinates
# horizontal_coordinates = 0
# vertical_coordiantes = 0

print(f'Initial coordinates: {horizontal}, {vertical}')

# determines child array index
## commenting to simplify with index
#if horizontal == 'a':
#  horizontal_coordinates = 0
#elif horizontal == 'b':
#  horizontal_coordinates = 1
#elif horizontal == 'c':
#  horizontal_coordinates = 2
#else:
#  print(f"Only A, B, C characters are allowed, you entered: {horizontal}")

# determines parent array index
## for some reason, this doesn't work, going with a dumber approach
#if vertical == 1:
#  vertical_coordinates = 0
#elif vertical == 2:
#  vertical_coordinates = 1
#elif vertical == 3:
#  vertical_coordinates = 2
#else:
#  print(f"Only 1, 2, 3 characters are allowed, you entered: {vertical}")

print(f"Ending coordinates: {vertical}, {horizontal_coordinates}")

map[vertical][horizontal_coordinates] = 'X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")