"""Highest and Lowest game

"""

# importing modules
from hl_logo import logo
from hl_logo import vs
from hl_data import data
import random
from clear import clear_screen


# Function Format the data to printable format
def format_data(account):
    """Function that formats the account data into printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


# Function to check if guess is correct
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns
        if they got it right.
    """
    if a_followers > b_followers:
        return guess == "a"  # Returns boolean "True" or "False"
    else:
        return guess == "b"  # Returns boolean "True" or "False"


# Display art on the screen
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)  # Precedence value of account_b for while loop

# Repeating the process until it failsa
while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    # Regenerate account_b if the users are equal
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]  # Get the follow account of each account
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear screen
    clear_screen()
    print(logo)

    # Give user feedback on their guess.
    # Scorekeeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"You're are wrong! Final score: {score}.")
        game_continue = False
