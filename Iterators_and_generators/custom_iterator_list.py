"""User define / Custom Iterator."""


class ListIterator:
    """Represent a list iterator."""

    def __init__(self, data_list: list[int]) -> None:
        self.data_list = data_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data_list):
            current_item = self.data_list[self.index]
            self.index += 1
            return current_item
        raise StopIteration


def main() -> None:
    """Run the main program."""
    even_numbers = [2, 4, 6]
    iterator = ListIterator(data_list=even_numbers)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator, "No Value"))


if __name__ == "__main__":
    main()
