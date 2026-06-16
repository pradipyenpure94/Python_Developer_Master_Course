"""Count uppercase letters."""


try:
    # Read file and its content.
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        # Count uppercase letters from file.
        count = sum(1 for ch in file_obj.read() if ch.isupper())
        print(f"Count uppercase letters: {count}")
except FileNotFoundError:
    print("File does not exist.")
