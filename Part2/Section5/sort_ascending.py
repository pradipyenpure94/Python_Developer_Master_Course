"""Sort ascending."""

from smallest_element import validate_numbers_list


def sort_list_ascending(numbers: list[int | float]) -> list[int | float]:
    """
    Return a new list, sorted in ascending order.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: A new list sorted in ascending order.
    """
    return sorted(numbers)


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 0, 1, 0, 1, 9, 9, 3]
        validate_numbers_list(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = sort_list_ascending(numbers=numbers)
        print(f"Ascending sorted list: {result}")


if __name__ == "__main__":
    main()
