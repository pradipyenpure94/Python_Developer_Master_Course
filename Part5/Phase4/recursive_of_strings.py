"""Recursive of strings."""


def recursive_of_strings(text: str) -> str:
    """Return the recursive of strings."""
    if text == "":
        return text
    return recursive_of_strings(text=text[1:]) + text[0]


if __name__ == "__main__":
    text = input("Enter the string: ").strip()
    result = recursive_of_strings(text=text)
    print(f"Reversed strings: {result}")
