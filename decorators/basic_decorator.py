"""Create a decorator that a print a message before calling a function."""


def my_decorator(func):
    """Simple decorator"""
    def wrapper():
        print("Function started.")
        func()
    return wrapper


@my_decorator
def greet():
    """Simple print message."""
    print("Hello Python")


greet()
