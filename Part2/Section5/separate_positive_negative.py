"""Separate positive and negative."""

from smallest_element import validate_numbers_list


def separate_positive_and_negative_numbers(
    numbers: list[int | float]
) -> tuple[list[int | float], list[int | float]]:
    """
    Return the separate positive and negative numbers
    from the input numbers list.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        tuple[list[int | float], list[int | float]]: A tuple containing the
        positive numbers and the negative numbers.
    """
    positive_nums = [number for number in numbers if number > 0]
    negative_nums = [number for number in numbers if number < 0]
    return positive_nums, negative_nums


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [-1, -2, 0, 1, 2, 3]
        validate_numbers_list(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        positive_nums, negative_nums = separate_positive_and_negative_numbers(
            numbers=numbers
        )
        print(f"Positive numbers: {positive_nums}")
        print(f"Negative numbers: {negative_nums}")


if __name__ == "__main__":
    main()
