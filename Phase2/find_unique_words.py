"""Find unique words in sentence."""

import string

sentence = "Python is good, so, im learning python"

words = sentence.casefold().split()
unique_words = set()

for word in words:
    clean_word = word.strip(string.punctuation)
    unique_words.add(clean_word)

print(f"Unique words: {unique_words}")
