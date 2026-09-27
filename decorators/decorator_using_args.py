"""Decorator supporting *args."""

from math import prod


def supporting_args(func):
    """Create a supporting *args."""
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        print(f"Function Arguments: {args}")
        result = func(*args)
        print(f"Result: {result}")
        return result
    return wrapper


@supporting_args
def addition(*args) -> float | int:
    """Return the addition of N numbers."""
    return sum(args)


@supporting_args
def multiplication(*args) -> float | int:
    """Return the multiplication of N numbers."""
    return prod(args)


if __name__ == "__main__":
    addition(10, 45, 0.5)
    multiplication(10, 5, 3)
