"""Linear search."""

from smallest_element import validate_numbers_list


def linear_search(numbers: list[int | float], target: int | float) -> int:
    """
    Return an index of the target value in a numbers list
    using linear search.

    Args:
        numbers (list[int | float]): Input numbers list.
        target (int | float): Value to search for. 

    Returns:
        int: Index of the target value if found; otherwise, -1.
    """
    for index, element in enumerate(numbers):
        if target == element:
            return index

    return -1


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 0, 1, 0, 1, 9, 9, 3]
        target = 3

        validate_numbers_list(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = linear_search(numbers=numbers, target=target)
        if result == -1:
            print(f"{target} not found.")
        else:
            print(f"{target} found at index {result}")


if __name__ == "__main__":
    main()
