# Program to convert a word to acronym
acronym = " "

word = input("Please Enter the word to be converted to an acronym: ")

word_new = word.split()  # A list of words

# Loop that creates an acronym
for letter in word_new:
    acronym += letter[0].upper()
print(acronym)
print(f"The acronym for {word} is {acronym}.")
