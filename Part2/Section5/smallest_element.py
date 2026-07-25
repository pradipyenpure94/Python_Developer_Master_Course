"""Smallest element."""

from largest_element import validate_numbers_list


def find_smallest_element(numbers: list[int | float]) -> int | float:
    """
    Return the smallest element in the input numbers list.

    Args:
        numbers (list[int | float]): User input numbers list.

    Returns:
        int | float: The smallest element in the input numbers list.
    """
    min_number = numbers[0]
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [10, 20, 40, 15, 30, 2, 5]
        validate_numbers_list(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = find_smallest_element(numbers=numbers)
        print(f"Smallest element: {result}")


if __name__ == "__main__":
    main()
