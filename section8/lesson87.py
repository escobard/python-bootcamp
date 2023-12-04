alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cypher_text = ""
  for char in text:
    # handle cases where shift takes index beyond alphabet length
    if alphabet.index(char) + shift > 25:
      shift_char = alphabet[(alphabet.index(char) + shift) - 26]
    else:
      shift_char = alphabet[alphabet.index(char) + shift]
    cypher_text += shift_char
  print(f"The encoded text is {cypher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
  decrypted_text = ""
  for char in text:
    ## no need to protect loop for negative index values, as negative index values are valid in python!
    shift_char = alphabet[alphabet.index(char) - shift]
    decrypted_text += shift_char
  print(f"The decoded text is {decrypted_text}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)