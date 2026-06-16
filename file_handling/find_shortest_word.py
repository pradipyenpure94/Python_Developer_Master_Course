"""Find shortest word."""


try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        words = file_obj.read().split()
        try:
            # Find shortest word
            shortest_word = min(words, key=len)
            print(f"Shortest word: {shortest_word}")
        except ValueError:
            print("File is empty.")
except FileNotFoundError:
    print("File does not exist.")
