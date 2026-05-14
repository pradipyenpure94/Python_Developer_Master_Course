"""Reverse words in string."""

text = input("Enter a string: ")

words = text.strip().split()
length = len(words)
reverse_words = []

for index in range(length - 1, -1, -1):
    reverse_words.append(words[index])

reversed_string = " ".join(reverse_words)
print(f"Reversed string: {reversed_string}")
