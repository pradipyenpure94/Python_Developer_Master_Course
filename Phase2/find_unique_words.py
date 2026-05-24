"""Find unique words in sentence."""

import string

sentence = "Python is good, so, im learning python"

unique_words = {word.strip(string.punctuation)
                for word in sentence.casefold().split()}
print(f"Unique words: {unique_words}")
