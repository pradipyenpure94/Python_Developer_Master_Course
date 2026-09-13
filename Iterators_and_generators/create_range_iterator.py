"""Design and develop a custom range() iterator."""


class RangeIterator:
    """Represent a range iterator."""

    def __init__(self, start: int, end: int) -> None:
        self.end = end
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value

        raise StopIteration


if __name__ == "__main__":
    numbers = RangeIterator(start=5, end=10)
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    print("In for loop")
    for number in numbers:
        print(number)
