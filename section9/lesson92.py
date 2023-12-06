# python dictionaries - almost identical to objects in js
## https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# sample dictionary
programming_dictionary = {
  "bug": "An error in a program",
  "function": "A piece of code you can easily call over and over again",
}

# retrieve an item from an index
print(programming_dictionary["function"])

# add / overwrite a new entry
programming_dictionary["test"] = 'A piece of code that validates that other code works'
print(programming_dictionary["test"])

# loop through a dictionary
for key in programming_dictionary:
  print(f"Key:{key}, Value: {programming_dictionary[key]}")

# wipe an empty dictionary
programming_dictionary = {}
print(programming_dictionary)

