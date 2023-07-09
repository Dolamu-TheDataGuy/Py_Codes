import random


def power_of(exponent):

    def decorator(func):

        def inner():

            return func() ** exponent

        return inner

    return decorator


@power_of(3)
def random_odd_digit():
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
