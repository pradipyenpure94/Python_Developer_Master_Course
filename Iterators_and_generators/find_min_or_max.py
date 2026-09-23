"""Find minimum/ maximum using a generator."""

from collections.abc import Iterator


def find_minimum_and_maximum_numbers(
    numbers: list[int]
) -> Iterator[tuple[int, int]]:
    """Find the minimum and maximum numbers."""
    yield min(numbers), max(numbers)


if __name__ == "__main__":
    nums = [1, 9, 9, 3]
    iterator = find_minimum_and_maximum_numbers(numbers=nums)
    min_number, max_number = next(iterator)
    print(f"Minimum number: {min_number}")
    print(f"Maximum number: {max_number}")
