"""Find duplicate characters."""

text = "pradip"

char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

duplicate_chars = set()
for key, value in char_freq.items():
    if value > 1:
        duplicate_chars.add(key)

print(f"Duplicate Chars: {duplicate_chars}")
