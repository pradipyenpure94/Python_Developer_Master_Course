"""Custom / User Defined Iterators."""


class NumberIterator:
    """Represent a number iterator."""

    def __init__(self, maximum) -> None:
        self.maximum = maximum
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


def main() -> None:
    """Run the main program."""
    numbers = NumberIterator(2)
    print(next(numbers))
    print(next(numbers))
    print(next(numbers, "No Value"))


if __name__ == "__main__":
    main()
