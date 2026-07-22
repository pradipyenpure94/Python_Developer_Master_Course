"""Count digits."""

from reverse_string import validate_string


def count_digits(text: str) -> int:
    """
    Return the total count of the digits in the input string.

    Args:
        text (str): User input number.

    Returns:
        int: The total count of the digits in the input string.
    """
    return sum(1 for char in text if char.isdigit())


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ").strip()
        validate_string(input_string=text)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = count_digits(text=text)
        print(f"Total count of digits: {result}")


if __name__ == "__main__":
    main()
