"""Find unique words in sentence."""

import string

sentence = "Python is good, so, im learning python"

words = sentence.casefold().split()
unique_words = set()
index = 0

while index < len(words):
    clean_word = words[index].strip(string.punctuation)
    unique_words.add(clean_word)
    index += 1

print(f"Unique words: {unique_words}")
