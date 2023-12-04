from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  # protect shift if a number greater than 26 is entered
  ## remainder is used as index position
  ### works for values lower than 26, since values lower than 26 are ignored 
  ### https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
  shift = shift % 26

  cypher_text = ""
  for char in text:
    # persists any character that is not in the alphabet 
    if char not in alphabet:
      shift_char = char
    elif direction == 'encode':
      # handle cases where shift takes index beyond alphabet length
      if alphabet.index(char) + shift > 25:
        shift_char = alphabet[(alphabet.index(char) + shift) - 26]
      else:
        shift_char = alphabet[alphabet.index(char) + shift]
    ## no need to protect loop for negative index values, as negative index values are valid in python!
    elif direction == 'decode':
      shift_char = alphabet[alphabet.index(char) - shift]
    cypher_text += shift_char
  print(f"The {direction} text is {cypher_text}")

print(logo)
 
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(direction, text, shift)
  # how to use an input & print statement together
  result = input("Type yes if you want to go again, type no if you don't want to:")
  if result == 'no':
    should_continue = False
    print('Goodbye')