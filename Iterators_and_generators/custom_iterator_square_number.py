"""Custom iterator square number."""


class SquareNumberIterator:
    """Represent a square number iterator."""

    def __init__(self, limit: int) -> None:
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current ** 2
            self.current += 1
            return value

        raise StopIteration


if __name__ == "__main__":
    try:
        numbers = SquareNumberIterator(5)
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
    except StopIteration:
        print("Error: StopIteration")
