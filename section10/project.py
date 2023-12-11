# calculator

from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# dictionary with key each operation and each calculator function as the value
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# instructor says function that can call itself is known as "recursion" - not to be confused with regression testing
def calculator():
  print(logo)
  ## inputs for the calculator
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input('Pick an operation from the line above: ')

    num2 = float(input("What's the next number?: "))

    # assign a function from the directory to the variable
    calculation_function = operations[operation_symbol]

    ## call the assigned function with the expected arguments
    answer = calculation_function(num1, num2)
    
    ## prints out the answer
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    ## syntax to use an input as a condition!
    if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      print("Calculation ended!")
      ## clears the terminal
      print("\033c")
      # calls calculator function so that it can re-set the program, known as functional regression
      calculator()

calculator()