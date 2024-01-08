# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# step 1 - grab names from files
with open('./names/invited_names.txt') as name_file:
  names = name_file.readlines()
  # print(names)

# step 2 - loop through all names in the file

  # step 4 - save example letter to variable
with open('./letters/starting_letter.txt') as example:
  letter = example.read()
  for name in names:
    # step 3 - remove line break from string
    name = name.strip('\n')
    # step 5 - replace [name] with name

    new_letter = letter.replace("[name]", name)
    # print(new_letter)

    # step 6 - write letter with name as a txt file to ready_to_send directory
    with open(f'./ready_to_send/{name}.txt', mode='w') as file:
     file.write(new_letter)