"""Decorator that modifies return a value."""


def uppercase(func):
    """Create uppercase decorator."""
    def wrapper(*args, **kwargs,):
        print(f"Function Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@uppercase
def message(name: str) -> str:
    """Return the text in uppercase."""
    return name.upper()


if __name__ == "__main__":
    print(message(name="Pradip"))
