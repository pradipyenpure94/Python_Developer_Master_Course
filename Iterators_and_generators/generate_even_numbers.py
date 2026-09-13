"""Generate Even Numbers from a List."""

from collections.abc import Generator


def generate_even_numbers(numbers: list[int]) -> Generator[int]:
    """Generate the even numbers."""
    for number in numbers:
        if number % 2 == 0:
            yield number


if __name__ == "__main__":
    numbers = [10, 15, 20, 25, 30, 35, 40]
    even_numbers = generate_even_numbers(numbers=numbers)
    print(next(even_numbers))
    print(next(even_numbers))
    print(next(even_numbers))
    print("In for loop")
    for number in even_numbers:
        print(number)
