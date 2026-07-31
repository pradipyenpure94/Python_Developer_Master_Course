"""Find intersection."""


def find_intersection(
    first_list: list[int],
    second_list: list[int]
) -> list[int]:
    """
    Return new list containing the common elements from the input numbers list.

    Args:
        first_list (list[int]): First input list.
        second_list (list[int]): Second input list.

    Returns:
        list[int]: A new list containing the common elements.
    """
    intersection_items = []
    second_set = set(second_list)
    for number in first_list:
        if number in second_set:
            intersection_items.append(number)

    return intersection_items


def main() -> None:
    """Run the Main Program."""
    even_nums = [2, 4, 6, 8, 10]
    prime_nums = [2, 3, 5, 7, 11]
    result = find_intersection(first_list=even_nums, second_list=prime_nums)
    print(f"Intersection list: {result}")


if __name__ == "__main__":
    main()
