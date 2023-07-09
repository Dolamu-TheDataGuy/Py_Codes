# How the Encryption works
# ABCDEFG

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Function to encode and decode a message
def caesar(start_text, shift_num, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_num *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # to cater for large magnitude of shift e.g 100, 1000
    caesar(start_text=text, shift_num=shift, cipher_direction=direction)
    c_key = input("Please enter 'yes' if you continue or 'no' if you wish to stop:\n")
    c_key = c_key.lower()

    if c_key == "yes":
        should_continue = True
    else:
        should_continue = False
