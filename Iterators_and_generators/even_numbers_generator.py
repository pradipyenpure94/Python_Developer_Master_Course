"""Even number generator."""

from collections.abc import Generator


def generate_even_numbers(limit: int) -> Generator[int]:
    """Generate the even numbers."""
    for number in range(limit):
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    even_numbers = generate_even_numbers(limit=10)
    print(next(even_numbers))
    print(next(even_numbers))
    print("In for loop")
    for number in even_numbers:
        print(number)
