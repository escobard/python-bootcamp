# functions with more than one input
def greet_with(name, location):
  print(f'Your name: {name}')
  print(f'Your location is {location}')
greet_with('Daniel', 'Calgary')

# function with pre-determined values
def greet_with_pre(name='Daniel', location='Calgary'):
  print(f'Your name: {name}')
  print(f'Your location is {location}')
greet_with_pre()

# calling a function with arguments - ignores argument order, cool!
greet_with(location="London", name="Juan")