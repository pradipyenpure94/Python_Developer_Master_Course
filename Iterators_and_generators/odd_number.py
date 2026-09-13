"""Odd Number Generator."""

from collections.abc import Generator


def generate_odd_numbers(limit: int) -> Generator[int]:
    """Generate the odd numbers."""
    for number in range(limit):
        if number % 2 == 1:
            yield number


if __name__ == "__main__":
    odd_numbers = generate_odd_numbers(limit=10)
    print(next(odd_numbers))
    print(next(odd_numbers))
    print(next(odd_numbers))
    print("In for loop")
    for number in odd_numbers:
        print(number)
