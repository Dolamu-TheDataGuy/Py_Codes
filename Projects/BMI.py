"""
Program that inteprets the Body Mass Index (BMI) of a person

Arg:
Height: height of Individual
Weight: Weight of Individual
BMI: Body Mass Index of Individual
"""

Height = int(input("enter your height in m: "))
Weight = int(input("enter your weight in kg: "))

BMI = (Weight/(Height ** 2))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, You are normal weight")
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}, You are overweight")
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, You are clinically obese")