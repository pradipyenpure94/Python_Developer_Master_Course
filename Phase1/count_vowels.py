"""Count vowels in a given string."""

text = input("Enter a string: ").strip().lower()

count = 0
index = 0
length = len(text)
while index < length:
    if text[index] in "aeiou":
        count += 1
    index += 1

print(f"Count vowels: {count}")
