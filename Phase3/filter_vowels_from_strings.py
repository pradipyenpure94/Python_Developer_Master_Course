"""Filter vowels from string."""


def filter_vowels_from_strings(words: list[str]) -> list[str]:
    """
    Return a new list containing the vowels from string list.

    Args:
        words (list[str]): Input words list.

    Returns:
        list[str]: A new list containing the vowels extracted from each string.
    """
    vowels = "aeiouAEIOU"
    return ["".join(filter(lambda char: char in vowels, word))
            for word in words]


if __name__ == "__main__":
    input_words = ["amit", "Pradip", "Akshay", "sandeep", "ramshet"]
    result = filter_vowels_from_strings(words=input_words)
    print(f"Filter vowels: {result}")
