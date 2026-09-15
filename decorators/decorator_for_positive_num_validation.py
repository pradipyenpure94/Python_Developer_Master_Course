"""Decorator for Positive Number Validation."""


def positive_number(func):
    """A simple positive decorator."""
    def wrapper(number):
        """To extend the positive decorator."""
        if number <= 0:
            return "Number must be positive."
        return func(number)
    return wrapper


@positive_number
def square_number(number):
    return number ** 2


if __name__ == "__main__":
    result = square_number(number=2)
    print(result)
