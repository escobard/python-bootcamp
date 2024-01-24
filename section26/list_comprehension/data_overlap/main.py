# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
with open('./file1.txt') as file_1:
  file_1_data = file_1.readlines()

with open('./file2.txt') as file_2:
  file_2_data = file_2.readlines()

file_1_data_as_integers = [int(integer) for integer in file_1_data]
file_2_data_as_integers = [int(integer) for integer in file_2_data]


print(file_1_data_as_integers)
print(file_2_data_as_integers)

result = [integer for integer in file_1_data_as_integers if integer in file_2_data_as_integers]

print(result)