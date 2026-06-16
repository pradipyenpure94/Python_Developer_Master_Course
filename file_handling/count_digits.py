"""Count digits."""


try:
    # Read file and its contents
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = file_obj.read()
        # Count digits from file.
        count = sum(1 for ch in data if ch.isdigit())
        print(f"Digits count: {count}")
except FileNotFoundError:
    print("File does not exist.")
