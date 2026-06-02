"""Check anagram strings."""


def is_anagram(text1: str, text2: str) -> bool:
    """
    Check whether two strings are anagrams.
    Args:
        text1 (str): First input string.
        text2 (str): Second input string.
    Returns:
        bool: True if two strings are anagrams, otherwise False.
    """
    text1 = text1.replace(" ", "").casefold()
    text2 = text2.replace(" ", "").casefold()
    return sorted(text1) == sorted(text2)


if __name__ == "__main__":
    first_string = input("Enter first input string: ")
    second_string = input("Enter second input string: ")
    if is_anagram(text1=first_string, text2=second_string):
        print("Strings are anagram.")
    else:
        print("Strings are not anagram.")
