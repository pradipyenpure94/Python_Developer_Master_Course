"""Custom iterator for square."""


class SquareIterator:
    """Represent an iterator for square."""

    def __init__(self, number: int):
        self.current = 1
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.number:
            value = self.current
            self.current += 1
            return value ** 2

        raise StopIteration


if __name__ == "__main__":
    iterator = iter(SquareIterator(number=5))

    for number in iterator:
        print(number)
