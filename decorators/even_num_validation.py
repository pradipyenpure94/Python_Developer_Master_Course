"""Decorator For Even Number Validation."""


def even_only(func):
    """Return the even number."""
    def wrapper(number):
        if number % 2 != 0:
            return "Number must be even."
        return func(number)
    return wrapper


@even_only
def square_number(number):
    """Return the square number."""
    return number ** 2


if __name__ == "__main__":
    result = square_number(4)
    print(result)
