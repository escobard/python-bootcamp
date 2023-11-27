#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
## can pre-define type of input by assigning a type before input declaration
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What tip percentage would you like to give?"))
how_many = int(input("How many people to split the bill?"))
bill_with_tip = total_bill + (total_bill * tip_percentage / 100)
bill_per_person = bill_with_tip / how_many
## .2f - We can use the %f formatter to specify the number of decimal numbers \
## to be returned when a floating point number is rounded up.
print(f"Each person should pay: ${bill_per_person:.2f}")
