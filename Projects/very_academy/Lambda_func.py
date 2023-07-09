def count(x):
    """
    Traditional function to add 10 to a number
    
    """
    y = x + 10
    return y


print(count(10))

add = (lambda x: x + 10)  # lambda argument: expression
print(add(10))

x = lambda y: y + 5
print(x(5))

x = lambda y, z: y + z
print(x(10, z=5))

num = (3, 555, 6, 9)

print(*num)


def sum(a, b, *arg):
    n = 0
    for i in arg:
        n += 1
    sum = a + b + n
    return sum


print(sum(5, 10, 1, 1, 1, 1, 1))
