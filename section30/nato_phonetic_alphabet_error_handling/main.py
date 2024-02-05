# Catch they key error when user enters illegal characters
# Provide a message to the user telling them illegal characters were found
# allow the user to re-type their input until a valid word is

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
# print(phonetic_alphabet)

# is_on = True
#
# while is_on:
#     word = input('Enter a word: ').upper()
#     try:
#         phonetic_list = [phonetic_alphabet[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         is_on = False
#         print(phonetic_list)
#
## instructor approach to avoid writing a loop
def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        phonetic_list = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()