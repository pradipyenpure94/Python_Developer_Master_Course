"""Find common elements between two lists."""

from typing import TypeVar
T = TypeVar("T")


def find_common_elements(list1: list[T], list2: list[T]) -> list[T]:
    """
    Return the common elements between two lists.

    Args:
        list1 (list[T]): First input list.
        list2 (list[T]): Second input list.

    Returns:
        list[T]: A list containing the common elements from both input lists.
    """
    common_elements = []
    list2_set = set(list2)
    for item in list1:
        if item in list2_set:
            common_elements.append(item)
    return common_elements


if __name__ == "__main__":
    first_input_list = [2, 4, 6, 8]
    print(f"First input list: {first_input_list}")
    second_input_list = [2, 3, 5, 7]
    print(f"Second input list: {second_input_list}")
    result = find_common_elements(list1=first_input_list,
                                  list2=second_input_list)
    print(f"Common elements: {result}")
