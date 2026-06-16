"""Search word in file."""

import string

search_word = "Company".casefold()

try:
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:

        data = file_obj.read().casefold()
        data = "".join(ch for ch in data if ch not in string.punctuation)
        contents = data.split()

        if search_word in contents:
            print("Found.")
        else:
            print("Not found.")

except FileNotFoundError:
    print("File does not exist.")
