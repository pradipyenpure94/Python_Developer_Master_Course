"""Find Longest word."""


try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = file_obj.read()
        words = data.split()
        try:
            longest_word = max(words, key=len)
            print(f"Longest word: {longest_word}")
        except ValueError:
            print("File is empty.")
except FileNotFoundError:
    print("File does not exist.")
