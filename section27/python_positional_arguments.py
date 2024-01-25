# sample function with positional python arguments
## create function that takes a dynamic number of arguments, sums all the arguments and returns the sum
def add(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum

print(add(2, 4, 11, 2, 4))