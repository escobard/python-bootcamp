## can check type of char with type()
## print(type(1))

## can convert types to other types
## new_num_char = str(1)

## print("Your name has " + new_num_char + " characters.")

# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# Don't change the code above
####################################
# Write your code below this line
print("Enter a 2 digit number:")
two_digit_number = input()
two_digit_number_to_string = str(two_digit_number)
result = int(two_digit_number_to_string[0]) + int(two_digit_number_to_string[1])
print("Result: " + str(result))