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

is_running = True


def check_resources(resources_to_check, coffee_choice):
  global is_running
  choice = menu[coffee_choice]
  out_of_ingredients = []
  has_ingredients = True
  for ingredient in choice['ingredients']:
    # print(f"Ingredient: {choice['ingredients'][ingredient]}")
    # print(f"Resource to check: {resources_to_check[ingredient]}")
    if choice['ingredients'][ingredient] > resources_to_check[ingredient]:
      print(f"Sorry there is not enough {ingredient}")
      out_of_ingredients.append(ingredient)
      has_ingredients = False
  ## simplified syntax for false statements, nice!
  if not has_ingredients:
    print(f"Machine shut down, not enough {''.join(out_of_ingredients)}")
    is_running = False


def coffee_machine():
  ## leverage global variable
  global is_running
  available_resources = resources
  while is_running:
    user_choice = input('What would you like? (espresso/latte/cappuccino):')
    if user_choice == 'off':
      is_running = False
    elif user_choice == 'print':
      print(f'Available resources: {available_resources}')
    else:
      print(user_choice)
      check_resources(available_resources, user_choice)

coffee_machine()
