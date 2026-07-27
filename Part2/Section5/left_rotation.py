"""Rotate list left."""

from smallest_element import validate_numbers_list


def rotate_list_by_left(
    numbers: list[int | float],
    position: int = 2
) -> list[int | float]:
    """
    Return a new list rotated to the left by the given position.

    Args:
        numbers (list[int | float]): Input numbers list.
        position (int, optional): Number of positions to rotate. Defaults to 2.

    Returns:
        list[int | float]: The left-rotated list.
    """

    if position <= 0:
        raise ValueError("Rotation position must be greater than zero.")

    position = position % len(numbers)
    return numbers[position:] + numbers[:position]


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        validate_numbers_list(numbers=numbers)
        result = rotate_list_by_left(numbers=numbers, position=4)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Left rotated list: {result}")


if __name__ == "__main__":
    main()
