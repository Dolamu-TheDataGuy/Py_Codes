import Calculate

num: int = Calculate.MY_NUM  # accessed the variable and the value of num becomes 2

add_value = Calculate.addition(2, 3)  # accessed addition function in Calculate.py
sub_value = Calculate.subtraction(3, num)  # accessed subtraction function in Calculate.py
mult_value = Calculate.multiplication(4, num)  # accessed multiplication function in Calculate.py

if __name__ == "__main__":
    print(add_value)
    print(sub_value)
    print(mult_value)