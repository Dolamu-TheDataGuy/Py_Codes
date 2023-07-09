"""Create a function that uses the list of numbers below to return a random card
"""
# import random function
import random

# import clear_screen function from clear.py module to clear screen
from clear import clear_screen


# Function to get card from card deck
def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Function to calculate sum of card
def calculate_score(cards):
    """Take a list of cards and return the score calculated
    from the cards
    """
    # check inside the calculate_score() for a blackjack(a hand with only 2 cards: ace + 10
    # +10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Function to compare user and computer score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


# Function that plays the blackjack game
def play_game():
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    # For loop to generate cards
    for run in range(2):
        new_card = deal_card()  # saves randomised card to variable "new_card"
        user_cards.append(new_card)  # add new_card to the user_card list
        computer_cards.append(deal_card())  # saves card from the deal_card function to the computer_cards

    while not is_game_over:
        # Call calculate_score(). If the computer or the user has a
        # blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # once the user is done, it's time to let the computer play. The computer should
    # Keep drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Ask user if they want to restart the game. if they answer yes, clear the console and start a new game of blackjack
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_screen()
    play_game()
