# calculator/calculations.py

def add(a, b):
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.
    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a, b):
    """Compute the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (float): A number representing the first minuend in the subtraction.
        b (float): A number representing the second minuend in the subtraction.
    Returns:
        float: A number representing the arithmetic difference between `a` and `b`.
        """
    return float(a - b)


def multiply(a, b):
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0
    Args:
        a (float): A number representing the first multiplicand in the multiplication.
        b (float): A number representing the second multiplicand in the multiplication.
    Returns:
        float: A number representing the product of `a` and `b`.
    """
    return float(a * b)


def divide(a, b):
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
    
    Args:
        a (float): A number representing the dividend in the division.
        b (float): A number representing the divisor in the division.
    Returns:
        float: A number representing the quotient of `a` and `b`
    Catches:
        ZeroDivisionError: An error that occurs when the divisor is `0`
        and alerts user to input b as number other than `0`.
    """
    try:
        a/b
    except ZeroDivisionError:
        print("b cannot be zero, please provide number other than zero")
    else:
        return float(a/b)
