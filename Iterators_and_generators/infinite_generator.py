"""Infinite Generator."""

from collections.abc import Iterator


def infinite_generator(number_start: int = 1) -> Iterator[int]:
    """Generate infinite numbers."""
    while True:
        yield number_start
        number_start += 1


if __name__ == "__main__":
    iterator = infinite_generator()

    for number in iterator:
        print(number)
