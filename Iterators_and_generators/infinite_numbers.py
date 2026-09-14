"""Infinite Number Generator."""

from collections.abc import Generator


def generate_infinite_numbers() -> Generator[int]:
    """Generate the infinite numbers."""
    n = 0

    while True:
        n += 1
        yield n

        if n == 10:
            break


if __name__ == "__main__":
    infinite_numbers = generate_infinite_numbers()
    print(next(infinite_numbers))
    print(next(infinite_numbers))
    print(next(infinite_numbers))
    print(next(infinite_numbers))
    print("In for loop")
    for number in infinite_numbers:
        print(number)
