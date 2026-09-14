"""Generic Decorator using *args."""


def decorator(func):
    """Simple decorator."""
    def warpper(*args):
        result = func(*args)
        return result
    return warpper


@decorator
def add(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


if __name__ == "__main__":
    print(f"Addition: {add(10, 20)}")
