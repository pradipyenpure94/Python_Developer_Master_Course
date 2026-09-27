"""Decorator that adds a prefix."""


def add_prefix(func):
    """Create decorator that adds a prefix."""
    def wrapper():
        result = func()
        return "Message: " + result
    return wrapper


@add_prefix
def get_message():
    """Return the message."""
    return "Python is powerful."


if __name__ == "__main__":
    print(get_message())
