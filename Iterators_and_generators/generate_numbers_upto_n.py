"""Generate numbers from 1 to N."""


from collections.abc import Iterator


def numbers(number: int) -> Iterator[int]:
    """Generate numbers from 1 to N."""
    for num in range(1, number + 1):
        yield num


if __name__ == "__main__":
    number = 5

    iterator = numbers(number=number)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
