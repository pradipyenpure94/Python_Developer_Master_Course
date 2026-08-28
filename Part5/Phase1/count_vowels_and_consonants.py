"""Count vowels and consonants."""

VOWELS = "aeiou"

try:
    text = input("Enter the string: ").strip().casefold()
    if not text:
        raise ValueError("String cannot be empty.")
    if not text.isalpha():
        raise ValueError(
            "Invalid input. Please enter only alphabet characters (A-Za-z).")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    vowels_count = 0
    consonants_count = 0

    for char in text:
        if char in VOWELS:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1

    print(f"Vowels count: {vowels_count}")
    print(f"Consonants count: {consonants_count}")
