# build a rock / paper / scissor game 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options_list = [rock, paper, scissors]

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_selection = int(input())
computer_selection = random.randint(0, 2)
result = ''

# instructor solution is a bit cleaner but more confusing condition comparison, leaving as is for readability
if user_selection == 0:
  if computer_selection == 0:
    result="You tied"
  elif computer_selection == 1:
    result="You lose"
  elif computer_selection == 2:
    result="You win"
elif user_selection == 1:
  if computer_selection == 0:
    result="You win"
  elif computer_selection == 1:
    result="You tied"
  elif computer_selection == 2:
    result="You lose"
elif user_selection == 2:
  if computer_selection == 0:
    result="You lose"
  elif computer_selection == 1:
    result="You win"
  elif computer_selection == 2:
    result="You tied"
else:
  print(f"Only 0, 1, 2 characters allowed. You entered: {user_selection}")
  exit()

user_result = options_list[user_selection]
computer_result = options_list[computer_selection]
print(user_result)
print("Computer chose:")
print(computer_result)
print(result)
