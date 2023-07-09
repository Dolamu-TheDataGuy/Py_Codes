from functools import wraps


def mapper(func):  # function that takes a function

    @wraps(func)
    def inner(list_of_strings):  # inner takes argument of inner function
        return [func(string) for string in list_of_strings]   # lc that applies the argument to primary function

    return inner


@mapper
def camelcase(s):
    """Turn a string likethis to a string LikeThis"""

    return "".join([word.capitalize() for word in s.split("_")])


names = [
    "rick_ross",
    "don_jazzy",
    "iron_man"
]

print(camelcase(names))
print(camelcase.__doc__)