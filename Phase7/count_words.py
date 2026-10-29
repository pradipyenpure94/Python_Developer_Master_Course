"""Count words and find the most frequent word in a sentence."""

sentence = "I love you. Pradip, I love you."
words = sentence.split(" ")
words_length = len(words)
print(f"Words Length: {words_length}")

frequency = dict()
for word in words:
    word = word.strip().casefold()
    frequency[word] = frequency.get(word, 0) + 1

most_frequent_word = max(frequency, key=frequency.get)
print(f"Most frequent word: {most_frequent_word}")
