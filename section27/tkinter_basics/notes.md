# advanced arguments in python

## default arguments
- we are able to set default arguments for functions
  - eg - my_function(c=3, a=1, b=2)

## *args positional arguments
- we can use *args to define multiple arguments in a function
  - *arguments - tells python to expect many functional arguments, we can call the argument itself anything we want
    - *arguments is passed in to the function as a tuple with the argument values
  - eg - add(*args):
    -   for n in args:
      - print(n)
    - add(3, 4, 5, 6) - pass in any number of arguments! 

## **kwargs key arguments
- we can use **kwargs to allow the function to pass in any number of keyword arguments
- **kwargs is passed in to the function as a dictionary with the argument key and value pairs
- example in section27/python_positional_arguments