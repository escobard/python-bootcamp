# You need to write a function that checks whether if the number passed into it is a prime number or not.
# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  ## checks if number is 1 or 0 before starting loop (neither are primary numbers)
  if number == 1 or number == 0:
          print("It's not a prime number.")
  else:
      ## starting a loop with a range, 1 or 0 number checked above
      for i in range(2, number):
          if number % i == 0:
              print("It's not a prime number.")
              ## break the loop the first time this result is found
              break  
      else:
          print("It's a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)