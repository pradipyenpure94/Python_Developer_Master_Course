"""Custom iterators from 1 to N numbers."""


class NumbersIterator:
    """Represent numbers iterator."""

    def __init__(self, end: int):
        self.current = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


iterator = NumbersIterator(end=5)
for number in iterator:
    print(number)
