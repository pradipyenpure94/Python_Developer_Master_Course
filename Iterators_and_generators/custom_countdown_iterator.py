"""Custom countdown iterator."""


class CountdownIterator:
    """Represent a custom count down iterator."""

    def __init__(self, number: int):
        self.current = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value

        raise StopIteration


if __name__ == "__main__":
    iterator = CountdownIterator(number=5)
    for number in iterator:
        print(number)
