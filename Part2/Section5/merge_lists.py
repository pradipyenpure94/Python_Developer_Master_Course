"""Merge lists."""

from smallest_element import validate_numbers_list


def merge_lists(*lists: list[int | float]) -> list[int | float]:
    """
    Merge the lists together from the input lists.

    Args:
        *lists (list[int | float]): User input lists.

    Returns:
        list[int | float]: The Merged list.
    """
    merged_lists = []

    for list_record in lists:
        validate_numbers_list(numbers=list_record)
        merged_lists.extend(list_record)

    return merged_lists


def main() -> None:
    """Run the Main Program."""
    try:
        even = [2, 4, 6, 8, 10]
        odd = [1, 3, 5, 7, 9]
        result = merge_lists(even, odd)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Merged Lists: {result}")


if __name__ == "__main__":
    main()
