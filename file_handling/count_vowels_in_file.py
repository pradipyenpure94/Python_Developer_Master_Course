"""Count vowels in file."""


vowels = "aeiouAEIOU"

try:
    # Read file and its content
    with open(file="file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        contents = file_obj.read()
        # Count vowels from file.
        vowels_count = sum(1 for ch in contents if ch in vowels)
        print(f"Vowels count: {vowels_count}")

except FileNotFoundError:
    print("File does not exist.")
