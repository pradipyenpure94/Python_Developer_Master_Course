"""Reverse string."""


def validate_string(input_string: str) -> None:
    """
    Validate the input string.

    Args:
        input_string (str): User input string.

    Raises:
        ValueError: If the string is empty.
    """
    if not input_string:
        raise ValueError("String cannot be empty.")


def reverse_string(input_string: str) -> str:
    """
    Return the reversed input string.

    Args:
        input_string (str): User input string.

    Returns:
        str: The reversed input string.
    """
    char_list = list(input_string)

    left = 0
    right = len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]

        left += 1
        right -= 1

    return "".join(char_list)


def main() -> None:
    """Run the Main Program."""
    try:
        input_string = input("Enter the string: ").strip()
        validate_string(input_string=input_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = reverse_string(input_string=input_string)
        print(f"Reversed string: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
