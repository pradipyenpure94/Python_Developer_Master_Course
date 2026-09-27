"""Validate integer arguments."""


def validate_integer(func):
    """Validate the integers."""

    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Argument must be integers.")
        return func(*args)
    return wrapper


@validate_integer
def addition(*args) -> int:
    """Return the addition of N numbers."""
    return sum(args)


if __name__ == "__main__":
    try:
        print(addition(10, 10))
    except TypeError as error:
        print(f"Error: {error}")
