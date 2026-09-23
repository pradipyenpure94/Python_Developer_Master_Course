"""Generate multiplication table using a generator."""

from collections.abc import Iterator


def multiplication_table(table: int) -> Iterator[int]:
    """Generate multiplication table."""
    for i in range(1, 11):
        yield table * i


if __name__ == "__main__":
    iterator = multiplication_table(table=5)
    for number in iterator:
        print(number)
