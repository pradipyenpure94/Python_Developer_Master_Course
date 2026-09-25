"""Decorator that prints before and after execution."""


def my_decorator(func):
    """Simple decorator."""
    def wrapper():
        print("Before function execution.")
        func()
        print("After function execution.")
    return wrapper


@my_decorator
def greeting():
    """Simple greeting."""
    print("Inside function execution.")


if __name__ == "__main__":
    greeting()
