"""Generate Fibonacci numbers using a generator."""

from collections.abc import Iterator


def fibonacci_numbers(limit: int) -> Iterator[int]:
    """Generate the Fibonacci numbers up to the given limit."""
    current_value, next_value = 0, 1
    for _ in range(1, limit + 1):
        yield current_value
        current_value, next_value = next_value, current_value + next_value


if __name__ == "__main__":
    iterator = fibonacci_numbers(limit=6)

    for number in iterator:
        print(number)
