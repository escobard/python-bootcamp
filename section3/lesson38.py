# You are going to write a program that tests the compatibility between two people.
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1.lower() + name2.lower()

t_count = combined_name.count('t')
r_count = combined_name.count('r')
u_count = combined_name.count('u')
e_count = combined_name.count('e')

true_count = t_count + r_count + u_count + e_count

l_count = combined_name.count('l')
o_count = combined_name.count('o')
v_count = combined_name.count('v')
e_count = combined_name.count('e')

love_count = l_count + o_count + v_count + e_count

string_count = str(true_count) + str(love_count)

int_count = int(string_count)

if int_count < 10 or int_count > 90:
  print(f"Your score is {int_count}, you go together like coke and mentos.")
elif int_count >= 40 and int_count <= 50:
  print(f"Your score is {int_count}, you are alright together.")
else: 
  print(f"Your score is {int_count}.")