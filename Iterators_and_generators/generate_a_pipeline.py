"""Generate pipeline."""

from collections.abc import Iterable, Iterator


def generate_numbers(numbers: list[int]) -> Iterator[int]:
    """Generate numbers."""
    for number in numbers:
        yield number


def filter_even_numbers(numbers: Iterable[int]) -> Iterator[int]:
    """Generate only even numbers."""
    for number in numbers:
        if number % 2 == 0:
            yield number


def square_numbers(numbers: Iterable[int]) -> Iterator[int]:
    """Generate the square of each number."""
    for number in numbers:
        yield number ** 2


if __name__ == "__main__":
    numbers_iterator = generate_numbers(numbers=[1, 2, 3, 4, 5])
    even_nums_iterator = filter_even_numbers(numbers=numbers_iterator)
    square_nums_iterator = square_numbers(numbers=even_nums_iterator)

    for number in square_nums_iterator:
        print(number)
