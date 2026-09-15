"""Decorator That Converts Result to Uppercase."""


def uppercase(func):
    """Convert the string to uppercase."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase
def to_uppercase(text):
    """To convert the uppercase string."""
    return text


if __name__ == "__main__":
    result = to_uppercase(text="Pradip")
    print(result)
