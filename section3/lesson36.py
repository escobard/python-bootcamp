# build an automatic pizza order program.
# Based on a user's order, work out their final bill.
print("Thank you for choosing Python Pizza Deliveries!")
print("What size pizza do you want? S, M, or L")
size = input()
print("Do you want pepperoni? Y or N")
add_pepperoni = input()
print("Do you want extra cheese? Y or N")
extra_cheese = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += + 2;
  else:
    bill +=  3;
if extra_cheese == "Y":
  bill += 1;

print(f"Your final bill is: ${bill}.")