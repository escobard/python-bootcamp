# Write a BMI calculator that returns bmi opinion on the weight vs height
# Enter your height in meters e.g., 1.55
print("What is your height in meters?")
height = float(input())
# Enter your weight in kilograms e.g., 72
print("What is your weight in kilograms?")
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
## changed height ** 2 to height * height for simplification
bmi = weight / height * height
your_bmi = "Your BMI is "
if bmi <= 18.5:
  print(f"{your_bmi}{bmi}, you are underweight.")
elif bmi < 25:
  print(f"{your_bmi}{bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"{your_bmi}{bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"{your_bmi}{bmi}, you are obese.")
elif bmi >= 35:
  print(f"{your_bmi}{bmi}, you are clinically obese.")