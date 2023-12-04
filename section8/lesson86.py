alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  cypher_text = []
  #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
  #e.g. 
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"

  for char in text:
    # handle cases where shift takes index beyond alphabet length
    if alphabet.index(char) + shift > 25:
      ## not sure if correct, but subtracting 25 - 1 to count for index position 0 
      shift_char = alphabet[(alphabet.index(char) + shift) - 26]
    else:
      shift_char = alphabet[alphabet.index(char) + shift]
    cypher_text += shift_char

  ##HINT: How do you get the index of an item in a list:
  #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

  ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
  print(f"The encoded text is {''.join(cypher_text)}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)