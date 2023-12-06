from logo import logo

bidder = {}
continue_auction = True
print(logo)
while continue_auction:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))

  bidder[name] = bid

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
  
  if (other_bidders == 'no'):
    highest_bidder = ''
    highest_bid = 0
    for key in bidder:
      if bidder[key] > highest_bid:
        highest_bid = bidder[key]
        highest_bidder = key
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    continue_auction = False
    

