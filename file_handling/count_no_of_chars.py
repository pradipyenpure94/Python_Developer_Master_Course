"""Count number of characters."""


try:
    # Open file and read its contents.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        content = file_obj.read()
        char_count = len(content)
        print(f"Count number of characters: {char_count}")
except FileNotFoundError:
    print("File does not exist.")
