"""Swap two numbers."""


def swap_two_numbers(first_number: int, second_number: int) -> tuple[int, int]:
    """
    Return the swap numbers, respectively,
    the first number and second number.

    Args:
        first_number (int): First input number.
        second_number (int): Second input number.

    Returns:
        tuple[int, int]: Swap the two input numbers.
    """
    first_number, second_number = second_number, first_number
    return first_number, second_number


def main() -> None:
    """Run the Main Program."""
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        first_number, second_number = swap_two_numbers(
            first_number=first_number,
            second_number=second_number
        )
        print("After swapping the numbers:")
        print(f"First number: {first_number}")
        print(f"Second number: {second_number}")


if __name__ == "__main__":
    main()
