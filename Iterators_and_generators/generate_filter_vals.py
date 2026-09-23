"""Generate filtered values from a list."""

from collections.abc import Iterator


def generate_filtered_values(numbers: list[int]) -> Iterator[int]:
    """Generate values greater than 20 from the list."""
    yield from filter(lambda x: x > 20, numbers)


if __name__ == "__main__":
    numbers = [10, 15, 20, 25, 30]

    iterator = generate_filtered_values(numbers=numbers)
    for number in iterator:
        print(number)
