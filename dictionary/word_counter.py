"""Word counter in sentence."""

import string

text = input("Enter a text: ")
clean_text = text.casefold().translate(
    str.maketrans('', '', string.punctuation))

words = clean_text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(f"Word counter: {count}")
