"""Check whether two strings are anagrams."""


def are_anagrams(text1: str, text2: str) -> bool:
    """
    Check whether two strings are anagrams.

    Args:
        text1 (str): First input text.
        text2 (str): Second input text.

    Returns:
        bool: True if the input strings are anagrams; otherwise, False.
    """
    return sorted(text1.casefold()) == sorted(text2.casefold())


if __name__ == "__main__":
    try:
        first_text = input("Enter first string: ").strip()
        second_text = input("Enter second string: ").strip()

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if are_anagrams(text1=first_text, text2=second_text):
            print("The strings are anagrams.")
        else:
            print("The strings are not anagrams.")
    finally:
        print("Operation completed.")
