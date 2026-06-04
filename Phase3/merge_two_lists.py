"""Merge two lists."""


def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Return a new list containing elements from both lists.

    Args:
        list1 (list[int]): First input list.
        list2 (list[int]): Second input list.

    Returns:
        list[int]: A new list containing elements from both input lists.
    """
    return [*list1, *list2]


if __name__ == "__main__":
    even = [2, 4, 6, 8, 10]
    odd = [1, 3, 5, 7, 9]
    result = merge_two_lists(list1=odd, list2=even)
    print(f"Merged Lists: {result}")
