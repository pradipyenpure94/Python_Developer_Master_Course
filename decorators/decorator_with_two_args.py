"""Decorator with two arguments."""


def decorator(func):
    """Simple decorator."""
    def wrapper(first_number, second_number):
        # print("Operation started.")
        result = func(first_number, second_number)
        # print("Operation completed.")
        return result
    return wrapper


@decorator
def add(first_number: int, second_number: int) -> int:
    """Addition of two numbers."""
    return first_number + second_number


@decorator
def subtraction(first_number: int, second_number: int) -> int:
    """Subtraction of two numbers."""
    return first_number - second_number


@decorator
def multiplication(first_number: int, second_number: int) -> int:
    """Multiplication of two numbers."""
    return first_number * second_number


if __name__ == "__main__":
    result = add(10, 15)
    print(f"Addition: {result}")
    result = subtraction(10, 5)
    print(f"Subtraction: {result}")
    result = multiplication(10, 6)
    print(f"Multiplication: {result}")
