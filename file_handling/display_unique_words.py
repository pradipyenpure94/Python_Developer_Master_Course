"""Display unique words."""

import string


try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = "".join(ch for ch in file_obj.read()
                       if ch not in string.punctuation).casefold()
        words = data.split()
        # Unique words from file.
        unique_words = set(words)
        print(f"Unique words: {unique_words}")
except FileNotFoundError:
    print("File does not exist.")
