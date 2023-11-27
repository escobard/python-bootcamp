# Write a program that checks if a given number is an odd or even number.
print("Which number do you want to check?")
number = int(input())
## Even numbers can be divided by 2 with no remainder
## The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
remainder = number % 2
if remainder == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")