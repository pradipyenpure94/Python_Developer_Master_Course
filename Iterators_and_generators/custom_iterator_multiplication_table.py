"""Custom iterator for multiplication tables."""


class MultiplicationTableIterator:
    """Represent a multiplication table iterator."""

    def __init__(self, table: int):
        self.table = table
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 10:
            value = self.current
            self.current += 1
            return value * self.table

        raise StopIteration


if __name__ == "__main__":
    iterator = iter(MultiplicationTableIterator(table=5))
    for number in iterator:
        print(number)
