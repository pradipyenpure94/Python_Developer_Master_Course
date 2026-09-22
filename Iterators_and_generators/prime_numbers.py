"""Custom iterator for prime numbers."""


def is_prime(number: int) -> bool:
    """Check whether a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class PrimeNumberIterator:
    """Represent a prime number iterator."""

    def __init__(self, max_value: int):
        self.current = 2
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_value:
            value = self.current
            self.current += 1
            if is_prime(value):
                return value

        raise StopIteration


if __name__ == "__main__":
    iterator = PrimeNumberIterator(max_value=13)

    for number in iterator:
        print(number)
