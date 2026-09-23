"""Generate squares even number."""

from collections.abc import Iterator


def generate_squares_of_even_numbers(limit: int) -> Iterator[int]:
    """Generate squares of even numbers up to the given limit."""
    yield from (x**2 for x in range(2, limit + 1, 2))


if __name__ == "__main__":
    iterator = generate_squares_of_even_numbers(limit=10)
    for number in iterator:
        print(number)
