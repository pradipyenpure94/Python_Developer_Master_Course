"""Generate numbers divisible by 3."""

from collections.abc import Iterator


def generate_numbers_divisible_by_3(limit: int) -> Iterator[int]:
    """Generate numbers divisible by 3."""
    yield from range(3, limit + 1, 3)


if __name__ == "__main__":
    iterator = generate_numbers_divisible_by_3(limit=25)

    for number in iterator:
        print(number)
