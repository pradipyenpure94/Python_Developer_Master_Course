"""Create a custom number iterators."""


class NumberIterator:
    """Represent a custom number iterator."""

    def __init__(self, limit: int) -> None:
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


if __name__ == "__main__":
    numbers = NumberIterator(limit=5)

    for number in numbers:
        print(number)
