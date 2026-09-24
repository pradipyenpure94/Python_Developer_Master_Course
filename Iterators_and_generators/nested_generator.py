"""Nested generators."""

from collections.abc import Iterator
from typing import TypeAlias

NestedList: TypeAlias = list[int | list["NestedList"]]


def flatten(nested_list: NestedList) -> Iterator[int]:
    """Flatten a nested list and generate its numbers."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    nested_data = [1, [2, 3, [4, 5]], 6, [7]]
    iterator = flatten(nested_list=nested_data)

    for number in iterator:
        print(number)
