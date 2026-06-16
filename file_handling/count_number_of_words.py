"""Count number of words."""


try:
    # Read file and its contents.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        count_words = len(file_obj.read().split())
        print(f"Count number of words: {count_words}")
except FileNotFoundError:
    print("File does not exist.")
