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
computer_selection = random.randint(1, 3) - 1
user_result = options_list[user_selection]
computer_result = options_list[computer_selection]
print(user_result)
print("Computer chose:")
print(computer_result)

if user_selection == 0:
  if computer_selection == 0:
    print("You tied")
  elif computer_selection == 1:
    print("You lose")
  elif computer_selection == 2:
    print("You win")
elif user_selection == 1:
  if computer_selection == 0:
    print("You win")
  elif computer_selection == 1:
    print("You tied")
  elif computer_selection == 2:
    print("You lose")
elif user_selection == 2:
  if computer_selection == 0:
    print("You lose")
  elif computer_selection == 1:
    print("You win")
  elif computer_selection == 2:
    print("You tied")
else:
  print(f"Only 0, 1, 2 characters allowed. You entered: {user_selection}")