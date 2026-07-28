"""Binary search."""

from smallest_element import validate_numbers_list


def binary_search(numbers: list[int | float], target: int | float) -> int:
    """
    Return an index of the target value in a sorted list using binary search.

    Args:
        numbers (list[int | float]): Sorted input numbers list.
        target (int | float): Value to search for.

    Returns:
        int: Index of the target value if found; otherwise -1.
    Raises:
        ValueError: If input numbers list is not sorted in ascending order.
    """
    if numbers != sorted(numbers):
        raise ValueError(
            "Input numbers list must be sorted in ascending order."
        )

    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if target < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [0, 0, 1, 1, 1, 3, 9, 9]
        target = 9

        validate_numbers_list(numbers=numbers)
        result = binary_search(numbers=numbers, target=target)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if result == -1:
            print(f"{target} not found.")
        else:
            print(f"{target} found at index {result}.")


if __name__ == "__main__":
    main()
