"""Replace vowel by *."""


def replace_vowel_by_star(text: str) -> str:
    """
    Return the, 'replace vowel by *' string

    Args:
        text (str): Input text.

    Returns:
        str: Replaced vowel by *
    """
    vowels = "AEIOUaeiou"
    return "".join("*" if char in vowels else char for char in text)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = replace_vowel_by_star(text=input_text)
    print(f"Replaced vowel by star (*): {result}")
