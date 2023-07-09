# 1. Create a dictionary in this format.
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)

alpha_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}


# Loop through string and generate dictionary
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
