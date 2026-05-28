"""Word frequency counter from file."""

import string
from collections import Counter

with open("Phase2/data_word_reading_file.txt", mode="r",
          encoding="utf-8") as file_obj:

    freq = {}
    text = file_obj.read().casefold()
    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    freq = Counter(words)

    for word, count in freq.most_common():
        if count > 2:
            print(f"{word} {count}")
