"""Group words by first letter."""

from collections import defaultdict

words = ["apple", "Attention", "orange", "otur", "cherry", "cat", "car"]

grouped_words = defaultdict(list)

for word in words:
    if word:
        word = word.casefold()
        grouped_words[word[0]].append(word)

print(f"Grouped words by first letter: {dict(grouped_words)}")
