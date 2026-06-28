"""Reverse a string."""


def reverse_string(text: str) -> str:
    """
    Return the reverse string.

    Args:
        text (str): Input text.

    Returns:
        str: Reversed string.
    """
    # Convert input text to a list.
    chars_list = list(text)

    left = 0
    right = len(chars_list) - 1

    while left < right:
        # Swap the characters
        chars_list[left], chars_list[right] = (chars_list[right],
                                               chars_list[left])
        left += 1
        right -= 1

    return "".join(chars_list)


if __name__ == "__main__":
    try:
        input_text = input("Enter a string: ").strip()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = reverse_string(text=input_text)
        print(f"Reversed string: {result}")
    finally:
        print("Operation completed.")
