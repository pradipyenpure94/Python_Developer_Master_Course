"""Find most frequenct character."""

text = "pradipii"

char_freq = {}

for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

max_frequent_char = max(char_freq, key=char_freq.get)
print(f"Most frequent character: {max_frequent_char}")
