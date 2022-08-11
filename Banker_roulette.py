import random
 
names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

num_names = len(names)

random_choice = random.randint(0, (num_names - 1))

person = names[random_choice]

#person = random.choice(names)

print(f"{person} is paying the bills")



