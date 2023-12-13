menu = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

def coffee_machine():
  is_running = True
  available_resources = resources
  while is_running:
    user_choice = input('What would you like? (espresso/latte/cappuccino):')
    if user_choice == 'off':
      is_running = False
    elif user_choice == 'print':
      print(f'Available resources: {available_resources}')
    else:
      print(user_choice)


coffee_machine()
