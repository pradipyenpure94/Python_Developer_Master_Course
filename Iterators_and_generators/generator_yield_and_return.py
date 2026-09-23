"""Generator with yield and return."""

from collections.abc import Generator


def countdown_with_message(number: int) -> Generator[int, None, str]:
    """Count down numbers and return a completion message."""
    while number > 0:
        yield number
        number -= 1
    return "All Done"


if __name__ == "__main__":
    iterator = countdown_with_message(number=5)
    try:
        while True:
            print(next(iterator))
    except StopIteration as error:
        print(error.value)
