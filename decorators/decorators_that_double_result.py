"""Decorator That Doubles The Result."""


def double_result(func):
    """Simple decorator."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


@double_result
def square_number(number):
    """Return the double result."""
    return number ** 2


if __name__ == "__main__":
    result = square_number(5)
    print(result)
