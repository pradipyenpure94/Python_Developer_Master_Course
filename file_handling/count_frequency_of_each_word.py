"""Count frequency of each word."""

import string


try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = file_obj.read().casefold()
        data = "".join(ch for ch in data if ch not in string.punctuation)
        words = data.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        print(f"Count frequency of each word: {freq}")
except FileNotFoundError:
    print("File does not exist.")
