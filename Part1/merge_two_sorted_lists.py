"""Merge two sorted lists."""


def merge_list(list1: list[int], list2: list[int]) -> list[int]:
    """
    Return a merge sorted lists.

    Args:
        list1 (list[int]): First input list.
        list2 (list[int]): Second input list.

    Returns:
        list[int]: A merged sorted list.
    """
    return sorted(list1 + list2)


if __name__ == "__main__":
    first_input_data = [2, 4, 6, 8]
    second_input_data = [1, 3, 5, 7]
    result = merge_list(list1=first_input_data, list2=second_input_data)
    print(f"Merged List: {result}")
