"""Function with keyword arguments."""


def add_numbers(first_number: int, second_number: int) -> int:
    """
    Return the addition of two numbers with keyword arguments.

    Args:
        first_number: First input number.
        second_input: Second input number.
    Returns:
        int: Addition of two numbers.
    """
    return first_number + second_number


if __name__ == "__main__":
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = add_numbers(
            second_number=second_number,
            first_number=first_number
        )
        print(f"Addition: {result}")
