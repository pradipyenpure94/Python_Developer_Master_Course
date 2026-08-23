"""Program 1: Convert a List into an Iterator.WAP to User Define iterator."""

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class ListIterator(Iterator[T]):
    """Represent a list iterator."""

    def __init__(self, data_list: list[T]) -> None:
        self.data_list = data_list
        self.index = 0

    def __iter__(self) -> "ListIterator":
        return self

    def __next__(self) -> T:
        if self.index < len(self.data_list):
            item = self.data_list[self.index]
            self.index += 1
            return item

        raise StopIteration


def main() -> None:
    """Run the main program."""
    numbers = [10, 20, 30]

    iterator = ListIterator(data_list=numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator, "No Value"))


if __name__ == "__main__":
    main()
