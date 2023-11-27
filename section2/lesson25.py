# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_weeks_to_90 = 4680
age_to_weeks = int(age) * 52
print(f"You have {total_weeks_to_90 - age_to_weeks} weeks left.")

# cleaner solution
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")