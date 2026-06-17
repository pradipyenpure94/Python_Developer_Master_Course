"""Display palindrome words from file."""


try:
    with open(file="file_handling/file1.txt", mode="r",
              encoding="utf-8") as file_obj:
        words = file_obj.read().split()

        for word in words:
            # Plaindrome words
            if word == word[::-1]:
                print(word)
except FileNotFoundError:
    print("File does not exist.")
