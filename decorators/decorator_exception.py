"""Decorator that log exception."""


def log_exception(func):
    """Log exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function name: {func.__name__}")
            print(f"Exception type: {type(e)}")
            print(f"Message: {e}")
            raise
    return wrapper


@log_exception
def division(first_number: float, second_number: float) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


if __name__ == "__main__":
    result = division(first_number=10, second_number=2)
    print(result)
