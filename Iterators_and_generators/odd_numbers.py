"""Generate odd numbers."""

from collections.abc import Iterator


def odd_numbers(number: int) -> Iterator[int]:
    """Generate odd numbers up to the given limit."""
    for num in range(1, number + 1, 2):
        yield num


if __name__ == "__main__":
    number = 10

    iterator = odd_numbers(number=number)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
