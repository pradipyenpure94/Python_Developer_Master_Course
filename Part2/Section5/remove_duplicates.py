"""Remove duplicates."""

from smallest_element import validate_numbers_list


def remove_duplicates(numbers: list[int | float]) -> list[int | float]:
    """
    Return the distinct numbers list with preserved order.

    Args:
        numbers (list[int | float]): User input numbers list.

    Returns:
        list[int | float]: A list of distinct numbers while preserving
        their original order.

    """
    unique_numbers = []
    seen = set()

    for number in numbers:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)

    return unique_numbers


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [2, 5, 6, 2, 3, 1, 2]
        validate_numbers_list(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = remove_duplicates(numbers=numbers)
        print(f"Unique numbers: {result}")


if __name__ == "__main__":
    main()
