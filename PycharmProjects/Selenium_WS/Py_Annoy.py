
hello: str = "hello world"


def add(x: int | float, y: int | float) -> int:
    return x + y


new_val: int | float = add(4, 5)
print(new_val)

str_int = {'one': 5, 'two': 7}
int_int = {1: 5, 2: 7}


def sum_dict(var: dict[int | float, int | float]) -> int:
    return sum(var[key] for key in var.keys())


sum_dict(str_int)
sum_dict(int_int)
