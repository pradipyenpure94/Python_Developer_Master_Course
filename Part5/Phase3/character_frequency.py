"""Count character frequency."""

text = "Pradip"

char_freq = {}

for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

print(f"Character frequency: {char_freq}")
