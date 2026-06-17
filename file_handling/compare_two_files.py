"""Compare two files."""

try:
    with open(file="file_handling/file1.txt", mode="r",
              encoding="utf-8") as file1_obj:
        f1 = file1_obj.read()

    with open(file="file_handling/file2.txt", mode="r",
              encoding="utf-8") as file2_obj:
        f2 = file2_obj.read()

    if f1 == f2:
        print("Same.")
    else:
        print("Different.")

except FileNotFoundError:
    print("One or more files do not exist.")
