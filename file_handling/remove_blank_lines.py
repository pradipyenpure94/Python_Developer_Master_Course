"""Remove blank lines."""


with open(file="file_handling/file1.txt", mode="r",
          encoding="utf-8") as src_file_obj,\
open(file="file_handling/file2.txt", mode="w",
     encoding="utf-8") as dest_file_obj:
    for line in src_file_obj.readlines():
        if line.strip():
            dest_file_obj.write(f"{line}")
