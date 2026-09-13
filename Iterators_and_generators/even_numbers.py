"""Custom iterator for Even Numbers."""


class EvenNumberIterator:
    """Represent an even number iterator."""

    def __init__(self, limit: int) -> None:
        self.current = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value

        raise StopIteration


if __name__ == "__main__":
    numbers = EvenNumberIterator(limit=10)
    print(next(numbers))
    print("For Loop")
    for number in numbers:
        print(number)
