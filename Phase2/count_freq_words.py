"""Count frequency of words in sentence."""
import string

text = "I love python and i am achive goal as python, developer job"

clean_text = "".join(char for char in text.casefold()
                     if char not in string.punctuation)
words = clean_text.split()
word_freq = {}
index = 0

while index < len(words):
    word = words[index]
    word_freq[word] = word_freq.get(word, 0) + 1

    index += 1

print(f"Count word frequency: {word_freq}")
