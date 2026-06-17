"""Copy only even lines."""

try:
    with open(file="file_handling/file1.txt", mode="r",
              encoding="utf-8") as src_file_obj,\
                open(file="file_handling/file2.txt", mode="w",
                     encoding="utf-8") as dest_file_obj:
        for i, line in enumerate(src_file_obj, start=1):
            if i % 2 == 0:
                dest_file_obj.write(line)
except FileNotFoundError:
    print("File does not exist.")
