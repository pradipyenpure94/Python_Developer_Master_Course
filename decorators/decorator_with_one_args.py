"""Decorator with one argument."""


def greet_decorator(func):
    """Simple greeting decorator."""
    def wrapper(name):
        """Simple decorator wrapper."""
        print("Greeting started.")
        func(name)
        print("Greeting ended.")
    return wrapper

@greet_decorator
def greet(name):
    """Simple greeting message."""
    print(f"Hello {name}...!")


if __name__ == "__main__":
    greet(name="Pradip")
