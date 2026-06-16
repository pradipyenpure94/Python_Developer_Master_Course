"""Count occurrence of a word."""

import string


word = "Python".casefold()

try:
    # Read file and it contents
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:

        data = "".join(char for char in file_obj.read()
                       if char not in string.punctuation)
        data = data.casefold()
        words = data.split()
        count_word_occurrence = words.count(word)

        print(f"Count word occurrence: {count_word_occurrence}")

except FileNotFoundError:
    print("File does not exist.")
