"""Create a custom iterator class."""


class MyIterator:
    """Represent a custom iterator."""
    def __init__(self, data):
        self.current = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.data):
            value = self.current
            self.current += 1
            return self.data[value]
        raise StopIteration


numbers = [1, 2, 3, 4, 15]
iterator = MyIterator(numbers)

for number in iterator:
    print(number)
