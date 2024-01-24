# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
#
# First, use list comprehension to convert the list_of_strings to a list of integers.
#
# Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.

list_of_strings = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55']

# convert to list of integers
list_of_integers = [int(number) for number in list_of_strings]

# convert to list that only contains even numbers
result = [integer for integer in list_of_integers if integer % 2 == 0]
