"""
An automatic pizza order program.

"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese?  ")

bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please enter either 'S', 'M', or 'L'")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is {bill}")