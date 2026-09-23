"""Generate countdown using a generator."""

from collections.abc import Iterator


def countdown_numbers(number: int) -> Iterator[int]:
    """Generate countdown numbers."""
    for num in range(number, 0, -1):
        yield num


if __name__ == "__main__":
    iterator = countdown_numbers(number=10)
    for number in iterator:
        print(number)
