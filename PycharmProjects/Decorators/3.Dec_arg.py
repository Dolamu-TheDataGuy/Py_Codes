import random


def power_of(arg):
    def decorator(func):

        def inner():
            return func() ** exponent

        return inner

    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@power_of(.5)
def random_odd_digit():
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
