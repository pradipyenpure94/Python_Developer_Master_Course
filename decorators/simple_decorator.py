"""Create a simple decorator."""


def my_decorator(func):
    """Simple basic decorator."""
    def wrapper(**kwargs):
        print("Before function execution.")
        func(**kwargs)
        print("After function execution.")
    return wrapper


@my_decorator
def greeting_message(name: str):
    """print message."""
    print(f"\nHello {name}...!\n")


if __name__ == "__main__":
    greeting_message(name="Pradip")
