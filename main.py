from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
continue_bid = True
bidder_data = {}

def new_bidder(name, bid):
  
  bidder_data[name] = bid

while continue_bid == True:

  new_name = input("What is your name? ")
  new_bid = int(input("What is your bid? $"))

  new_bidder(new_name, new_bid)
  others = input("Are there other users who want to bid? Y/N").lower()
  if others == "n":
    continue_bid = False
  elif others == "y":
    clear()


max_bidder = max(bidder_data)
max_bid = bidder_data[max_bidder]
  
print(f"The winner is {max_bidder} with ${max_bid}!")