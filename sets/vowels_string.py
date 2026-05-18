"""Vowels in string using set"""

vowels = {"a", "e", "i", "o", "u"}
text = "Programming"
found = set()

for char in text:
    if char.casefold() in vowels:
        found.add(char)

print(f"Vowels found in string: {found}")
