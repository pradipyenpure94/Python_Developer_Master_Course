"""Read first line."""


try:
    # Read first line from the file.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        first_line = file_obj.readline()
        print(f"Read first line: {first_line}")
except FileNotFoundError:
    print("File does not exist.")
