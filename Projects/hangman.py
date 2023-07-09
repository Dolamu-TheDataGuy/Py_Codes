#Step Import module
import random


#Variables to be used in code
end_of_game = False  #Variable for while loop control
from hangman_word import word_list    #imported words from the hangman_word module
chosen_word = random.choice(word_list)    #use the random module to guess a word
word_len = len(chosen_word)    #get the length of the word

lives = 6  #lives for gallow

from hangman_art import logo,stages
print(logo)
print(f"The chosen word is {chosen_word}")

#Create an empty list called display:
display = []
for num in range(word_len):
    display.append("_")
print(display)


while not end_of_game:
    guess = input("Guesss a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    #Replace the dash with the chosen word
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #If guess is not a letter in the choosen_word, then reduce 'lives' by 1.
    if guess not in chosen_word:
        lives -= 1
        #if lives goes down to 0 then the game shouls stop and it should print "You lose"
        if lives == 0:
            end_of_game = True
            print("You lose.")


    #Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    #check if user has gotten all the letters
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    #from hangman_art import stages
    print(stages[lives])