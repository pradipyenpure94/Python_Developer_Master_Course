"""Count frequency of characters in string."""

import string

text = "Pradip"
clean_text = "".join(char for char in text.casefold()
                     if char not in string.punctuation and not char.isspace())

char_freq = {}

for char in clean_text:
    char_freq[char] = char_freq.get(char, 0) + 1

print(f"Count character frequency: {char_freq}")
