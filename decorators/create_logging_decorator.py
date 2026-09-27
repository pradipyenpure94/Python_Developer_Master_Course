"""Create a logging decorator."""


def logger(func):
    """Create a logging decorator."""
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        result = func(*args)
        print(f"Result: {result}")
        return result
    return wrapper


@logger
def addition(*args) -> float:
    """Return the addition of N numbers."""
    return sum(n for n in args)


if __name__ == "__main__":
    addition(10, 20, 30.5, 40.8)
