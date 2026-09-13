"""Creating our own iterator."""


class NumberIterator:
    """Represent a number iterator."""

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
    try:
        numbers = NumberIterator(3)
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
        print(next(numbers))
    except StopIteration:
        print("Error: StopIteration")
