"""
Program that uses the concept of dictionaries
and function to device a calculator.

"""
#Add

def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def division(n1, n2):
    return n1/n2

sign = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

def calculator():
    num1 = float(input("Whats the first number?: "))

    for symbol in sign:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_sign =  input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        calculator_func = sign[operation_sign]
        answer = calculator_func(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or start all again.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
            