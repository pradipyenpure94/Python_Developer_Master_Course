"""Count vowels, consonants, digits and special characters."""


def count_character_type(text: str) -> tuple[int, int, int, int]:
    """
    Return the count of vowels, consonants, digits and special characters.

    Args:
        text (str): Input text.

    Returns:
        tuple[int, int, int, int]: Count of vowels, consonants, digits and
        special characters.
    """
    vowels = {"a", "e", "i", "o", "u"}

    vowels_count = consonants_count = digits_count = special_chars_count = 0

    for char in text:
        if char.isalpha():
            if char.casefold() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

        elif char.isdigit():
            digits_count += 1

        elif not char.isspace():
            special_chars_count += 1

    return vowels_count, consonants_count, digits_count, special_chars_count


if __name__ == "__main__":
    try:
        input_text = input("Enter a string: ").strip()

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        (vowels_count,
         consonants_count,
         digits_count,
         special_chars_count) = count_character_type(text=input_text)
        print(f"Vowels count: {vowels_count}\n"
              f"Consonants count: {consonants_count}\n"
              f"Digits count: {digits_count}\n"
              f"Special characters count: {special_chars_count}")
    finally:
        print("Operation completed.")
