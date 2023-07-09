def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print("Error: invalid argument")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

    
for i in range(5):
    print(i, end='')
    print("aba")