"""Count unique vowels in string."""

text = "India"

vowels = {"a", "e", "i", "o", "u"}

count = len({char for char in text.casefold() if char in vowels})
print(f"Count unique vowels: {count}")
