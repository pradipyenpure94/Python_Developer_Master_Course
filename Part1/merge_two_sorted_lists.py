"""Merge two sorted lists."""


def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Return a merged sorted list.

    Args:
        list1 (list[int]): First input list.
        list2 (list[int]): Second input list.

    Returns:
        list[int]: A merged sorted list.
    """
    merged_list = list1 + list2
    n = len(merged_list)

    for i in range(n):
        found = False
        for j in range(n -i -1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = (merged_list[j + 1],
                                                      merged_list[j])
                found = True

        if not found:
            break
    return merged_list


if __name__ == "__main__":
    first_input_data = [2, 4, 6, 8]
    second_input_data = [1, 3, 5, 7]
    result = merge_sorted_lists(list1=first_input_data, list2=second_input_data)
    print(f"Merged List: {result}")
