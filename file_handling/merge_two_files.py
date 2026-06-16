"""Merge two files."""


try:
    # First file
    # Read file and its content.
    with open(file="file_handling/file1.txt", mode="r",
              encoding="utf-8") as file1_obj:
        f1 = file1_obj.read()

    # Second file
    # Read file and its content.
    with open(file="file_handling/file2.txt", mode="r",
              encoding="utf-8") as file2_obj:
        f2 = file2_obj.read()

    # Merge two files.
    with open("file_handling/merge_file.txt", mode="w",
              encoding="utf-8") as merged_file_obj:
        merged_file_obj.write(f"{f1}\n{f2}")

except FileNotFoundError:
    print("The first file or second file does not exist.")
