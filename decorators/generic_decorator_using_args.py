"""Generic Decorators using *args."""


def decorator(func):
    """Simple decorator."""
    def wrapper(*args):
        return func(*args)
    return wrapper


@decorator
def multiply(first_number, second_number):
    """Return the multiplication of two numbers."""
    return first_number * second_number


@decorator
def addition(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


if __name__ == "__main__":
    result = multiply(10, 52)
    print(f"Multiplication: {result}")

    result = addition(10, 5)
    print(f"Addition: {result}")
