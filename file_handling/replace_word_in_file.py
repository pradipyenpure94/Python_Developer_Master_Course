"""Replace word in file."""

try:
    with open(file="file_handling/file1.txt", mode="r", encoding="utf-8") as file_obj:
        data = file_obj.read()
    with open(file="file_handling/file1.txt", mode="w", encoding="utf-8") as obj:
        data = data.replace("python", "PYTHON")
        obj.write(data)
except FileNotFoundError:
    print("File does not exist.")
