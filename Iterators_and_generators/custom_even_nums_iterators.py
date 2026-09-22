"""Custom iterator for Even numbers."""


class EvenNumbers:
    """Represent an iterator for even numbers."""

    def __init__(self, end: int):
        self.current = 2
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
    iterator = EvenNumbers(end=10)
    for number in iterator:
        print(number)
