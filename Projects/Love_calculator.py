name1 = input("Please input first name: ")
name2 = input("Please input second name: ")


comb_name = name1 + name2
lower_case_string = comb_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

love_score = int(love_score)

print(love_score)

if (love_score < 10) or (love_score) > 90:
    print("Your love score is {love_score}, you go together like coke and menthos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")