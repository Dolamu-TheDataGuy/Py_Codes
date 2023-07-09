import time
 
def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " " + "took" + " " + str((end-start)*1000) + " " + "milliseconds")
        return len(result)
    return inner



@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number ** 3)
    return result

array = range(1,10000)
calc_square(array)
calc_cube(array)
