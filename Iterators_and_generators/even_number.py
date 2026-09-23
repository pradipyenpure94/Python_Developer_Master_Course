"""Generate even numbers."""

from collections.abc import Iterator


def even_numbers(number: int) -> Iterator[int]:
    """Generate even numbers."""
    for num in range(2, number + 1, 2):
        yield num


if __name__ == "__main__":
    even_nums_iterator = even_numbers(number=10)

    print(next(even_nums_iterator))
    print(next(even_nums_iterator))
    print(next(even_nums_iterator))
    print(next(even_nums_iterator))
    print(next(even_nums_iterator))
