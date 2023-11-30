# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_of_even_numbers = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    sum_of_even_numbers += number
print(sum_of_even_numbers)

# simplified solution from instructor, by better using the range function
even_numbers = 0
for number in range(2, target + 1, 2):
    even_numbers += number
print(even_numbers)