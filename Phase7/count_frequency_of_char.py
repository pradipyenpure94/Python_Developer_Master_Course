"""Count the frequency of every character."""


text = "Pradip".casefold()
frequency = dict()

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(f"Count of characters: {frequency}")
