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
processing_transaction = True
money = 0

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
    print(f"Machine shut down, not enough {', or '.join(out_of_ingredients)}")
    is_running = False

def process_coins(cost):
  global processing_transaction
  global money

  print('Please insert coins.')

  quarters = int(input('How many Quarters?'))
  dimes = int(input('How many Dimes?'))
  nickles = int(input('How many Nickles?'))
  pennies = int(input('How many Pennies?'))
  money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

  if cost > money:
    print(f"Sorry, ${money} is not enough money. Money refunded")
    processing_transaction = False

def process_transaction(coffee_choice):
  global resources
  for ingredient in coffee_choice['ingredients']:
    resources[ingredient] -= coffee_choice['ingredients'][ingredient]
  if money > coffee_choice['cost']:
    print(f'Your change is ${round(money - coffee_choice['cost'], 2)}')


def coffee_machine():
  ## leverage global variables
  global is_running
  global processing_transaction
  global resources

  while is_running:
    user_choice = input('What would you like? (espresso/latte/cappuccino):')
    if user_choice == 'off':
      is_running = False
    elif user_choice == 'print':
      print(f'Available resources: {resources}')
    else:
      coffee_choice = menu[user_choice]
      print(f"You have selected a {user_choice}")
      check_resources(coffee_choice)
      processing_transaction = True
      while processing_transaction and is_running:
        process_coins(coffee_choice['cost'])
        process_transaction(coffee_choice)
        print(f"Here is your {user_choice} ☕. Enjoy!")
        processing_transaction = False

coffee_machine()
