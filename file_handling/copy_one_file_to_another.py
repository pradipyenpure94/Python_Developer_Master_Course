"""Copy one file to another."""


try:
    # Source file.
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as source_file_obj:
        source_file_data = source_file_obj.read()

    # Destination file.
    # Copy data from source file to destination file.
    with open(file="file_handling/destination_file.txt", mode="w",
              encoding="utf-8") as destination_file_obj:
        destination_file_obj.write(source_file_data)

except FileNotFoundError:
    print("Source file does not exist.")
