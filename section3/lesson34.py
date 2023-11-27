# Write a program that works out whether if a given year is a leap year. 
# This is how you work out whether if a particular year is a leap year.
## on every year that is divisible by 4 with no remainder
## except every year that is evenly divisible by 100 with no remainder
## unless the year is also divisible by 400 with no remainder
print("Enter year:")
year = int(input())
not_leap = "Not leap year"
leap = "Leap year"
if year % 4 == 0:
  if year % 100 > 0:
    print(leap)
  elif year % 100 == 0:
    if year % 400 == 0:
      print(leap)
    elif year % 400 > 0:
      print(not_leap)
else:
  print(not_leap)