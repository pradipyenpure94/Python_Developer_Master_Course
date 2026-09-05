"""Function using *args."""


def addition(*numbers: int) -> int:
    """Return the addition of numbers."""
    return sum(numbers)


if __name__ == "__main__":
    result = addition(10, 20, 30, 40)
    print(f"Addition: {result}")
