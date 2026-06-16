"""Read file line by line."""


try:
    # Open file in read mode.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        # Read file line by line.
        for line in file_obj:
            print(line.strip())
except FileNotFoundError:
    print("File does not exist.")
