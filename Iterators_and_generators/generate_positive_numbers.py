"""Generate Only Positive Numbers."""

from collections.abc import Generator


def generate_positive_numbers(numbers: list[int]) -> Generator[int]:
    """Generate the positive numbers."""
    for number in numbers:
        if number > 0:
            yield number


if __name__ == "__main__":
    numbers = [-10, 20, -5, 30, 0, 40, -2]
    positive_numbers = generate_positive_numbers(numbers=numbers)
    print(next(positive_numbers))
    print(next(positive_numbers))
    print("In for loop")
    for number in positive_numbers:
        print(number)
