"""Function to reverse string."""


def reverse_string(text: str) -> str:
    """
    Return the reverse a string.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed a string.
    """
    return "".join(reversed(text))


if __name__ == "__main__":
    try:
        text = input("Enter the string: ").strip()
        if not text:
            raise ValueError("String cannot be empty.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = reverse_string(text=text)
        print(f"Reversed string: {result}")
