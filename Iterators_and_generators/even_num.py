"""Generate even numbers using generator expression."""

from collections.abc import Iterator


def even_numbers(limit: int) -> Iterator[int]:
    """Generate even numbers up to the given limit."""
    yield from range(2, limit + 1, 2)


if __name__ == "__main__":
    iterator = even_numbers(limit=10)
    for number in iterator:
        print(number)
