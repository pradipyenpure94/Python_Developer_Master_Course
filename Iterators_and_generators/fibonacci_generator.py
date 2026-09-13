"""
Fibonacci Generator.
Create generator for Fibonacci numbers.
"""
from collections.abc import Generator


def generate_fibonacci_numbers(limit: int) -> Generator[int]:
    """Generate the fibonacci numbers."""
    first_number, second_number = 0, 1
    for _ in range(limit):
        yield first_number
        first_number, second_number = (
            second_number, first_number + second_number
        )


if __name__ == "__main__":
    fibonacci_numbers = generate_fibonacci_numbers(limit=5)
    print(next(fibonacci_numbers))
    print(next(fibonacci_numbers))
    print("In for loop")
    for number in fibonacci_numbers:
        print(number)
