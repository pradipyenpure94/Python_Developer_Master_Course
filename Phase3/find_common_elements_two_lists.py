"""Find common elements in two list."""


def find_common_elements(list1: list[int], list2: list[int]) -> list[int]:
    """
    Return the elements common to both lists.

    Args:
        list1 (list[int]): First input numbers list.
        list2 (list[int]): Second input numbers list.

    Returns:
        list[int]: Elements present in both lists.
    """
    list2 = set(list2)
    return [number for number in list1 if number in list2]


if __name__ == "__main__":
    prime_numbers = [2, 3, 5, 7, 11, 13]
    odd_numbers = [1, 3, 5, 7, 9, 11, 13]
    result = find_common_elements(list1=prime_numbers, list2=odd_numbers)
    print(f"Common elements: {result}")
