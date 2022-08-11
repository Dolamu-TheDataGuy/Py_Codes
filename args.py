def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)

    for arg in argv:
        print("another arg through *argv :", arg)


test_var_args("Dolzy", "python","Java","Javascript","Golang","Ruby","Rust")

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key} is {value}")

greet_me(name = "John")


def test_args_kwargs(arg1, arg2, arg3):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"arg3: {arg3}")

args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
