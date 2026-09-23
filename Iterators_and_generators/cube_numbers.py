"""Generate cubes using a generator."""

from collections.abc import Iterator


def cube_numbers(limit: int) -> Iterator[int]:
    """Generate cube numbers up to the given limit."""
    for num in range(1, limit + 1):
        yield num ** 3


if __name__ == "__main__":
    iterator = cube_numbers(limit=5)

    for number in iterator:
        print(number)
