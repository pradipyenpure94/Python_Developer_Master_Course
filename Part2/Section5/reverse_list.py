"""Reverse list."""

from smallest_element import validate_numbers_list


def reverse_list(numbers: list[int | float]) -> list[int | float]:
    """
    Return the reversed input list.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: The reversed list.
    """
    return [numbers[index] for index in range(len(numbers) - 1, -1, -1)]


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        validate_numbers_list(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = reverse_list(numbers=numbers)
        print(f"Reversed List: {result}")


if __name__ == "__main__":
    main()
