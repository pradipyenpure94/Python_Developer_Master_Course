"""Count vowels in list of strings."""

words = ["apple", "banana", "cherry", "Orange", "Banana", "Kiwi"]

vowels = "aeiou"
vowels_count = sum(1 for word in words for char in word
                   if char.casefold() in vowels)
print(f"Vowels count: {vowels_count}")
