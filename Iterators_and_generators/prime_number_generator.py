"""Prime Number Generator."""

from collections.abc import Generator


def is_prime_number(number: int) -> bool:
    """Check whether a number is a prime."""
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def generate_prime_numbers(limit: int) -> Generator[int]:
    """Generate the prime numbers."""
    for number in range(limit):
        if is_prime_number(number=number):
            yield number


if __name__ == "__main__":
    prime_numbers = generate_prime_numbers(limit=20)
    try:
        print(next(prime_numbers))
        print(next(prime_numbers))
        print(next(prime_numbers))
        print("In for loop")
        for number in prime_numbers:
            print(number)
    except StopIteration:
        print("Error: StopIteration")
