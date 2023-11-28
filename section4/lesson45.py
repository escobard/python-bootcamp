import random
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

## subtract by 1 to account for array index count starting at 0
length = len(names) - 1;
random_number = random.randint(0, length)
print(f"{names[random_number]} is going to buy the meal today!")