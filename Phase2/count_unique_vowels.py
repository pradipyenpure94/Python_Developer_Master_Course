"""Count unique vowels in string."""

text = "India"

vowels = {"a", "e", "i", "o", "u"}
count = 0
input_text_set = set(text.casefold())

for char in input_text_set:
    if char in vowels:
        count += 1

print(f"Count unique vowels: {count}")
