"""Remove Duplicate Values Using a Generator."""

from collections.abc import Generator


def generate_unique_numbers(numbers: list[int]) -> Generator[int]:
    """Remove duplicate numbers from list."""
    seen = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
            yield number


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 20, 40, 30]
    unique_numbers = generate_unique_numbers(numbers=numbers)
    print(next(unique_numbers))
    print(next(unique_numbers))
    print("In for loop")
    for number in unique_numbers:
        print(number)
