"""Replace multiple spaces with a single space."""


def replace_spaces_with_single_space(text: str) -> str:
    """
    Replace multiple spaces with a single space.

    Args:
        text (str): Input text.

    Returns:
        str: Input text with multiple spaces replaced by a single space.
    """
    return " ".join(text.split())


if __name__ == "__main__":
    try:
        input_text = input("Enter text: ").strip()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = replace_spaces_with_single_space(text=input_text)
        print(f"Text after replacing multiple spaces: {result}")
    finally:
        print("Operation completed.")
