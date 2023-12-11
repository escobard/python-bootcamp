#In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# Create a new function called days_in_month()

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  leap = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  ## if chosen month is february and it is a leap year, return 29, because feb has 29 days during a leap year
  if leap and month - 1 == 1:
    return 29
  else:
    return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year")) # Enter a year
month = int(input("Enter a month")) # Enter a month
days = days_in_month(year, month)
print(days)

