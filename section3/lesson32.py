print("Welcome to the rollercoaster!");
height = int(input("What is your height in cm? "));

# traditional if statement in python
if height >= 120:
    # indentation starts the block scope of the if statement 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
      print("Please pay $5.")
    elif age <= 18:
      print("Please pay $7.")
    elif age < 22:
      print("Please pay $7.")
    else:
      print("Please pay $12.")
else:
    # indentation starts the block scope of the if statement 
    print("Sorry, you have to grow taller before you can ride.")
