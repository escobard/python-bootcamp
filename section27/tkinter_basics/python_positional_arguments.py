# sample function with positional python arguments
## create function that takes a dynamic number of arguments, sums all the arguments and returns the sum
def add(*args):
  print(args)
  sum = 0
  for arg in args:
    sum += arg
  return sum

print(add(2, 4, 11, 2, 4))

# sample function with keyword python arguments
## create function that takes a dynamic number of keyword arguments
def calculate(n, **kwargs):
  print(kwargs)
  ## can access each of the key/values with a loop
  ## for key, value in kwargs.items():

  ## can access key names individually
  n += kwargs["add"]
  n *= kwargs["multiply"]
  return n


print(calculate(2, add=3, multiply=5))