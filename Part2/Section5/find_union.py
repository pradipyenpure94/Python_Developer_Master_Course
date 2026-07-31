"""Find union."""


def find_union(
    first_list: list[int],
    second_list: list[int]
) -> list[int]:
    """
    Return new list containing the unique elements from the both input list.

    Args:
        first_list (list[int]): First input list.
        second_list (list[int]): Second input list.

    Returns:
        list[int]: A new list containing the unique elements.
    """
    return list(set(first_list + second_list))


def main() -> None:
    """Run the Main Program."""
    even_nums = [2, 4, 6, 8, 10]
    prime_nums = [2, 3, 5, 7, 11]
    result = find_union(first_list=even_nums, second_list=prime_nums)
    print(f"Union list: {result}")


if __name__ == "__main__":
    main()
