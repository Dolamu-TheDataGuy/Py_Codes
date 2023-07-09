#Data Types
#Integer: 2, 50, 10,000,000
#Float: 0.6, 50.78, 6000.5
#Strings: "Hello", "Camera"
#Boolean: "True" and "False"


#Type error
print("Ade" + 2)
print(len(12345))

#Type conversion
Amount = int(33.33) #converts the float 33.33 to an integer 33
Amount = int("33")  #converts the string "33" to an integer 33

#Mathematical operations
#Addition: +
#Subtraction: -
#Multiplication: *
#Division: /
#Exponentiation: **
#Floor division: //
#Modulus: %

#Number manipulation & String Manipulation
print(int(8/5))  #8/5 would by default give you a float.
score = 0
score +=1 #shorthand for score = score + 1
score *=1 #shorthand for score = score * 1
score /=1 #shorthand for score = score / 1
score -=1 #shorthand for score = score - 1

#Mathematical Operator on String
print("The function of" + " " + "addition is to" + " " + "different strings")
print("Hello" * 10)

#f-string and formatting
print(f"your score is {score}")
print("your score is {}".format(score))
