"""Generate squares using a generator."""

from collections.abc import Iterator


def square_numbers(limit: int) -> Iterator[int]:
    """Generate square numbers up to the given limit."""
    for num in range(limit + 1):
        yield num ** 2


if __name__ == "__main__":
    iterator = square_numbers(limit=5)

    for number in iterator:
        print(number)
