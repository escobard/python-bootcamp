# raise allows us to raise our own exceptions
## similar to JS throw New Error()
# raise KeyError("This is an error that I made up")

height = float(input("Height:"))
weight = int(input("Weight:"))

## checks that height is no more than 3 meters
if height > 3:
  raise ValueError("Human height should not exceed 3 meters")

bmi = weight / height ** 2
