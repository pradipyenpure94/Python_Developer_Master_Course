"""Custom iterator for odd numbers."""


class MyOddNumbersIterator:
    """Represent a custom odd numbers iterator."""

    def __init__(self, end: int):
        self.current = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 2
            return value
        raise StopIteration


if __name__ == "__main__":
    iterator = MyOddNumbersIterator(end=5)
    try:
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
    except StopIteration:
        print("Iterator is exhausted.")
