"""Add two numbers."""


def addition(first_number: int, second_number: int) -> int:
    """
    Return the addition of two numbers.

    Args:
        first_number (int): First input number.
        second_number (int): Second input number.

    Retursn:
        int: Addition of two numbers.
    """
    return first_number + second_number


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
        result = addition(
            first_number=first_number,
            second_number=second_number
        )
        print(f"Addition: {result}")


if __name__ == "__main__":
    main()
