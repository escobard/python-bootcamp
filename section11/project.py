############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project < -----

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# simulate standard deck of cards
## game does not actually remove cards once chosen, but could be improved in the future
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_running = True

def checkWinner(your_cards, computer_cards):

  print(f"Your Cards {your_cards}, current score: {sum(your_cards)}")
  print(f"Computer score is {sum(computer_cards)}")
  
  if sum(your_cards) > 21:
    print(f"Bust - You lose!")
    is_running = False  
  elif sum(computer_cards) > 21:
    print(f"Bust - Computer loses, you win!")
    is_running = False
  elif sum(your_cards) == 21:
    print(f"Blackjack - you win!")
  elif sum(computer_cards) == 21:
    print(f"Blackjack - Computer wins!")
  elif sum(your_cards) > sum(computer_cards):
    print(f"You win!")
  elif sum(your_cards) < sum(computer_cards):
    print(f"Computer wins!")
  elif sum(your_cards) == sum(computer_cards):
    print(f"It's a tie!")

while is_running:
  print(logo)
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play == 'y':
    your_cards = []
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))

    computer_cards = []
    computer_cards.append(random.choice(cards))

    print(f"Your Cards {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card {computer_cards[0]}")

    if sum(your_cards) == 21:
      print(f"Blackjack - You win!")
      is_running = False
    elif sum(your_cards) > 21:
      print(f"Bust - You lose!")
      is_running = False
    
    ## can only draw once in this version of the game
    draw = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw == 'n':

      computer_cards.append(random.choice(cards))
      checkWinner(your_cards, computer_cards)
      is_running = False
    else:
      computer_cards.append(random.choice(cards))
      your_cards.append(random.choice(cards))
      checkWinner(your_cards, computer_cards)
      is_running = False  
  else:
    is_running = False
    print('Thanks for playing!')