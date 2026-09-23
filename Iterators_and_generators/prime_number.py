"""Generate prime numbers using a generator."""

from collections.abc import Iterator
from prime_numbers import is_prime


def prime_numbers(limit: int) -> Iterator[int]:
    """Generate prime numbers up to the given limit."""

    for number in range(2, limit + 1):
        if is_prime(number=number):
            yield number


if __name__ == "__main__":
    iterator = prime_numbers(limit=20)
    for number in iterator:
        print(number)
