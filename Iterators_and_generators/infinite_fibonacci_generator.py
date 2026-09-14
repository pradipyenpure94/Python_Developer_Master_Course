"""Infinite Fibonacci Generator."""

from collections.abc import Generator
from itertools import islice


def generate_infinite_fibonacci_numbers() -> Generator[int]:
    """Generate the infinite fibonacci numbers."""
    first_number, second_number = 0, 1
    while True:
        yield first_number
        first_number, second_number = (
            second_number, first_number + second_number
        )


if __name__ == "__main__":
    fibonacci_numbers = generate_infinite_fibonacci_numbers()
    for number in islice(fibonacci_numbers, 15):
        print(number)
