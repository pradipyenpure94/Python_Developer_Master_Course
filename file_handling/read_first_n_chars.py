"""Read first N characters."""


N = 10

try:
    # Read first N characters from the file.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        first_n_chars = file_obj.read(N)
        print(f"Read first N characters: {first_n_chars}")
except FileNotFoundError:
    print("File does not exist.")
