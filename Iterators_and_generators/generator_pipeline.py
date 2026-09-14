"""Generator Pipeline."""

from collections.abc import Generator, Iterator


def generate_numbers(limit: int) -> Generator[int]:
    """Generate the numbers."""
    for number in range(1, limit + 1):
        yield number


def generate_square_numbers(numbers: Iterator[int]) -> Generator[int]:
    """Generate the square numbers."""
    for number in numbers:
        yield number ** 2


def generate_even_numbers(numbers: Iterator[int]) -> Generator[int]:
    """Generate the even numbers."""
    for number in numbers:
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    numbers = generate_numbers(limit=6)
    square_numbers = generate_square_numbers(numbers=numbers)
    even_numbers = generate_even_numbers(numbers=square_numbers)

    for number in even_numbers:
        print(number)
