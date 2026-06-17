"""Reverse file content."""


try:
    with open(file="file_handling/file1.txt", mode="r", encoding="utf-8") as file_obj:
        data = file_obj.read()
    reverse_file_content = data[::-1]
    print(reverse_file_content)
except FileNotFoundError:
    print("File does not exist.")
