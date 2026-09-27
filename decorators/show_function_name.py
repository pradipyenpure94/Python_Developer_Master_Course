"""Decorator that prints the function name."""


def show_function_name(func):
    """print function name."""
    print(f"Function name: '{func.__name__}' function")

    def wrapper(*args, **kwargs):
        print("Addition of two numbers:")
        result = func(*args, **kwargs)
        return result
    return wrapper


@show_function_name
def addition(first_number: float, second_number: float) -> float:
    """Return the addition of two numbers."""
    return first_number + second_number


if __name__ == "__main__":
    first_number = 10
    second_number = 5
    result = addition(first_number=first_number, second_number=second_number)
    print(f"Addition: {result:.2f}")
