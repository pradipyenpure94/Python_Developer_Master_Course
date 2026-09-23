"""Convert list comprehension into generator expression."""

from collections.abc import Iterator


def square_numbers(limit: int) -> Iterator[int]:
    """Generate square numbers."""
    yield from (x * x for x in range(1, limit + 1))


if __name__ == "__main__":
    iterator = square_numbers(limit=5)

    for number in iterator:
        print(number)
