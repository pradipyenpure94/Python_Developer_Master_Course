"""Custom iterator for Fibonacci numbers."""


class FibonacciIterator:
    """Represent a custom Fibonacci iterator."""

    def __init__(self, max_value: int):
        self.max_value = max_value
        self.current = 0
        self.next_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration

        current = self.current
        self.current, self.next_value = (
            self.next_value, self.current + self.next_value
        )

        return current


if __name__ == "__main__":
    iterator = iter(FibonacciIterator(max_value=8))
    for number in iterator:
        print(number, end=",")
