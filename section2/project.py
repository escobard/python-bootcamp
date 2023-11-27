#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?")
tip_percentage = input("What tip percentage would you like to give?")
how_many = input("How many people to split the bill?")
total_bill = int(total_bill)
tip_percentage = int(tip_percentage)
how_many = int(how_many)
bill_with_tip = total_bill + (total_bill * tip_percentage / 100)
bill_per_person = bill_with_tip / how_many
print(f"Each person should pay: ${bill_per_person:.2f}")
