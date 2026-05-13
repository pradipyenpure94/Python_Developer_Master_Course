"""Count vowels in a given string"""

text = input("Enter a string: ").strip()

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(f"Count vowels: {count}")
