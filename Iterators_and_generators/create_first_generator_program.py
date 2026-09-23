"""Create your first generator program."""

from collections.abc import Iterator


def even_numbers() -> Iterator[int]:
    """Generate even numbers."""
    yield 2
    yield 4
    yield 6


if __name__ == "__main__":
    iterator = iter(even_numbers())
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
