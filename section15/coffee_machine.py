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
processing_coins = True


def check_resources(coffee_choice):
  global is_running
  global resources

  out_of_ingredients = []
  has_ingredients = True

  for ingredient in coffee_choice['ingredients']:
    # print(f"Ingredient: {choice['ingredients'][ingredient]}")
    # print(f"Resource to check: {resources_to_check[ingredient]}")
    if coffee_choice['ingredients'][ingredient] > resources[ingredient]:
      print(f"Sorry there is not enough {ingredient}")
      out_of_ingredients.append(ingredient)
      has_ingredients = False

  ## simplified syntax for false boolean checks, nice!
  if not has_ingredients:
    print(f"Machine shut down, not enough {''.join(out_of_ingredients)}")
    is_running = False

def process_coins(cost):
  global processing_coins

  print('Please insert coins.')

  quarters = int(input('How many Quarters?'))
  dimes = int(input('How many Dimes?'))
  nickles = int(input('How many Nickles?'))
  pennies = int(input('How many Pennies?'))
  total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

  if cost > total:
    print(f"Sorry, ${total} is not enough money. Money refunded")
    processing_coins = False
  else:
    if total > cost:
      print(f'Your change is {round(total - cost, 2)}')

def process_transaction():
  global resources


def coffee_machine():
  ## leverage global variables
  global is_running
  global processing_coins
  global resources

  while is_running:
    user_choice = input('What would you like? (espresso/latte/cappuccino):')
    coffee_choice = menu[user_choice]
    if user_choice == 'off':
      is_running = False
    elif user_choice == 'print':
      print(f'Available resources: {resources}')
    else:
      print(f"You have selected a {user_choice}")
      check_resources(coffee_choice)

      while processing_coins and is_running:
        process_coins(coffee_choice['cost'])
        process_transaction()

coffee_machine()
