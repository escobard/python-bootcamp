alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO - combine encrypt() and decrypt() functions into a single function called caesar()

def caesar(direction, text, shift):
  cypher_text = ""
  for char in text:
      if direction == 'encode':
        # handle cases where shift takes index beyond alphabet length
        if alphabet.index(char) + shift > 25:
          shift_char = alphabet[(alphabet.index(char) + shift) - 26]
        else:
          shift_char = alphabet[alphabet.index(char) + shift]
      elif direction == 'decode':
        shift_char = alphabet[alphabet.index(char) - shift]
    cypher_text += shift_char
  print(f"The {direction} text is {cypher_text}")

caesar(direction, text, shift)