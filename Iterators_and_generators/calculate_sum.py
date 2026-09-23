"""Calculate sum using a generator expression."""


from collections.abc import Iterator


def calculate_sum(number: int) -> Iterator[int]:
    """Calculate the sum of integers from 1 to the given input number."""
    yield sum(x for x in range(1, number + 1))


if __name__ == "__main__":
    iterator = calculate_sum(number=10)
    print(next(iterator))
