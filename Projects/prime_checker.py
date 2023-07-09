def prime_checker(number):
    if number == 1 or number == 0:
        print("it is not a prime number")
    else:
        is_prime = True
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
        if is_prime:
            print("it is a prime number.")
        else:
            print("It is not a prime number.")
            
n = int(input("Check this number: "))
prime_checker(number = n)