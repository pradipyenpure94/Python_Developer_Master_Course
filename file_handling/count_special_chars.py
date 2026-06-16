"""Count special chars."""


import string

try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:

        data = file_obj.read()
        # Count special characters
        count = sum(1 for ch in data if ch in string.punctuation)
        print(f"Count special characters: {count}")

except FileNotFoundError:
    print("File does not exist.")
