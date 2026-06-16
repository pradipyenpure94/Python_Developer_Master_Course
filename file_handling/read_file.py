"""Read entire file."""


try:
    # Open file in read mode
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        content = file_obj.read()
        print(content)
except FileNotFoundError:
    print("File does not exist.")
