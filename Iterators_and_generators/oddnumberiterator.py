"""Create a custom odd number iterator."""


class OddNumberIterator:
    """Represent an odd number iterator."""

    def __init__(self, limit: int) -> None:
        self.current = 1
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
    numbers = OddNumberIterator(limit=10)
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    print("In for loop")
    for number in numbers:
        print(number)
