"""Guessing Number Game
"""
import random

print("Welcome to the Number Guessing Game!")
print("Thinking of a number between 1 and 100.")
difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ")

#Function that guesses number and compares with answer
def game(num):
    answer = random.randint(1, 100)
    while  num >= 1:
        print (f"You have {num} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"got it! The answer was {answer}")
            break
        if num == 1:
            print(f"You loose, number is {answer}")
            break  
        if guess > answer:
            print("Too high\nGuess again")
            num -= 1
        if guess < answer:
            print("Too low\nGuess again")
            num -= 1

def set_difficulty():
    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        game(10)
    elif difficulty == "hard":
        game(5)

set_difficulty()




