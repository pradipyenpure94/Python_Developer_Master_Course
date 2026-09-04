"""Function to find maximum of three numbers."""


def find_max_number(
    first_number: int,
    second_number: int,
    third_number: int
) -> int:
    """
    Return a maximum number from these three numbers.

    Args:
        first_number: First input number.
        second_number: Second input number.
        third_number: Third input number.

    Returns:
        int: The maximum number.
    """
    if first_number >= second_number and first_number >= third_number:
        return first_number
    elif second_number >= third_number and second_number >= first_number:
        return second_number
    else:
        return third_number


if __name__ == "__main__":
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        third_number = int(input("Enter the third number: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        max_number = find_max_number(
            first_number=first_number,
            second_number=second_number,
            third_number=third_number
        )

        print(f"Maximum number: {max_number}")
