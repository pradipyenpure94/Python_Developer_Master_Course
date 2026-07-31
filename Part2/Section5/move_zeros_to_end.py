"""Move zeros to end."""

from smallest_element import validate_numbers_list


def move_zeros_to_end(numbers: list[int | float]) -> list[int | float]:
    """
    Return the zeros to end with numbers.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: A new list with all non-zero elements first,
        followed by all zeros.
    """
    non_zeros = []
    zeros = []

    for num in numbers:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)

    return non_zeros + zeros


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 0, 2, 3, 0, 5]
        validate_numbers_list(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    else:
        result = move_zeros_to_end(numbers=numbers)
        print(f"After moving zeros to end: {result}")


if __name__ == "__main__":
    main()
