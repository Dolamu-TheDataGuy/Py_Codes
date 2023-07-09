import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["!", '#', '@', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the Password generator!!!")
pass_letters = int(input("How many letters would you like in your password\n"))
pass_symbols = int(input("How many symbols would yoy like in your password?\n"))
pass_numbers = int(input("How many numbers would you like?\n"))

# make an empty string to hold the password
password_list = []
password = ""

# using the random module and for loop to get our password
for char in range(1, pass_letters + 1):
    rand_char = random.choice(letters)
    password_list += rand_char  # password = password + rand_char

for num in range(1, pass_numbers + 1):
    rand_num = random.choice(nums)
    password_list += rand_num

for symbol in range(1, pass_symbols + 1):
    rand_symbol = random.choice(symbols)
    password_list += rand_symbol

print(password_list)

# Make Password more complex
random.shuffle(password_list)

print(password_list)
for char in password_list:
    password += char

print(f"Your password is {password}")
