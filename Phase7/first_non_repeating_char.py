"""Find the first non-repeating character."""

frequency = dict()
text = "welcome"

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

non_repeating_char = ""
for char, count in frequency.items():
    if count == 1:
        non_repeating_char = char
        break

print(f"First non-repeating char: {non_repeating_char}")
