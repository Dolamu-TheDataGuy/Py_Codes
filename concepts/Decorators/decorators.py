"""Decorators"""


def decorator(func):

    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was invoked with arg {args=} and {kwargs=}")
        return func(*args, **kwargs)
    
    return wrapper


@decorator
def sqr(no):
    return no ** 2

ans = sqr(5)

print(ans)