"""Create iterator for numbers in a range."""


class RangeIterator:
    """Create a custom range() iterator."""

    def __init__(self, start: int, end: int, step: int = 1):

        if step == 0:
            raise ValueError("Step cannot be zero.")

        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start >= self.end:
            raise StopIteration

        if self.step < 0 and self.start <= self.end:
            raise StopIteration

        value = self.start
        self.start += self.step
        return value


if __name__ == "__main__":
    try:
        iterator = RangeIterator(start=1, end=5)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        for number in iterator:
            print(number)
