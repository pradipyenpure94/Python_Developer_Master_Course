"""Count unique vowels in string."""

text = "India"

vowels = {"a", "e", "i", "o", "u"}
count = 0
input_text_list = list(set(text.casefold()))
index = 0

while index < len(input_text_list):
    char = input_text_list[index]
    if char in vowels:
        count += 1
    index += 1

print(f"Count unique vowels: {count}")
