"""Validate multiple arguments."""

from math import prod


def validate_multiple_arguments(func):
    """Create decorator that validate multiple arguments."""
    def wrapper(*args):
        print(f"Function arguments: {args}")
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Argument must be number.")
        return func(*args)
    return wrapper


@validate_multiple_arguments
def multiplication(*args) -> int | float:
    """Return the multiplication of N numbers."""
    return prod(args)


if __name__ == "__main__":
    try:
        result = multiplication(10, 2.5)
    except TypeError as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")
