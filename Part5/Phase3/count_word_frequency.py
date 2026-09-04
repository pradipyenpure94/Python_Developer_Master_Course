"""Count word frequency."""


text = "My name is Pradip. I love pune. Pradip lovebirds."

words_freq = {}
words = text.split()

for word in words:
    words_freq[word] = words_freq.get(word, 0) + 1

print(f"Words frequency: {words_freq}")
