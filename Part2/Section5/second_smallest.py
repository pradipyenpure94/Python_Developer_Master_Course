"""Second smallest."""

from smallest_element import validate_numbers_list


def second_smallest_element(numbers: list[int | float]) -> int | float:
    """
    Return the second smallest distinct element in the input numbers list.

    Args:
        numbers (list[int | float]): User input numbers list.

    Returns:
        int | float: The second smallest distinct element
        in the input numbers list.
    """
    if len(set(numbers)) < 2:
        raise ValueError("Two distinct numbers must be in the numbers list.")

    first_number = second_number = float('inf')

    for number in numbers:
        if number < first_number:
            second_number = first_number
            first_number = number
        elif number < second_number and number != first_number:
            second_number = number

    return second_number


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [12, 11, 141, 13, 15, 18, 17]
        validate_numbers_list(numbers=numbers)
        result = second_smallest_element(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Second smallest: {result}")


if __name__ == "__main__":
    main()
