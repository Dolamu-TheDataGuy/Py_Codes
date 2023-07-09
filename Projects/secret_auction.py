from clear import clear_screen
from auction_art import logo

print(logo)

# Secret Auction Code.
bid_dict = {}
bidding = False


# Function to obtain the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding:
    name = input("What is your name?: ")
    price = int(input("What is yout bid price in $?: "))
    bid_dict[name] = price
    to_continue = input("is there any other bidder? Type 'yes' or 'no'.  ")

    if to_continue == "no":
        bidding = True
        find_highest_bidder(bid_dict)
    elif to_continue == "yes":
        clear_screen()
