import sheety

print("Welcome to Dolamu Flight Club")
print("We find the best flight deals and email you")
first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()
email = input("What is your email? ").lower()
ag_email = input("Please enter your email again: ").lower()
while email != ag_email:
  print("Password mismatch")
  email = input("Please enter your email: ")
  if email.lower() == "quit" or email.lower() == "exit":
    exit()
  ag_email = input("Please enter your email again: ")
  if ag_email.lower() == "quit" or ag_email.lower() == "exit":
    exit()
print("Welcome to the club")

sheety.post_new_row(first_name=first_name, last_name=last_name, email=email)
