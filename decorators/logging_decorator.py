"""Logging Decorator."""


def logging_decorator(func):
    """A simple logging decorator."""
    def wrapper(*args, **kwargs):
        """Extend decorator."""
        print(f"Function started: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function completed: {func.__name__}")
        return result
    return wrapper


@logging_decorator
def cube_number(number):
    """Return the cube of number."""
    return number ** 3


if __name__ == "__main__":
    result = cube_number(number=2)
    print(f"Cube of number: {result}")
