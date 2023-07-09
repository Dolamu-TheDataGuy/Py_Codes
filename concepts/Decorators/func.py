from functools import wraps

def decorator(func):
    #args put arguments in a tuple
    @wraps(func)
    def wrapper(*args, **kwargs):
        no = args[0]
        if not isinstance(no, int):
            raise ValueError
        
        print(f"{func.__name__} was invoked with arg {args=} and {kwargs=}")
        return func(*args, **kwargs)
    
    return wrapper

@decorator
def mine(a):
    return a * 8


ans = mine(45)
print(ans)