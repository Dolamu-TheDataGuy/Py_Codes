"""
Program to check if a year is a Leap year.

"""

year = int(input("what year do you want to check?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year!")
    else:
        print(f"{year} is a leap year!")    
else:
    print(f"{year} is not a leap year!")

