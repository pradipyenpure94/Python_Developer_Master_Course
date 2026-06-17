"""Find most frequent word."""


try:
    with open(file="file_handling/file1.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = file_obj.read()

    freq = {}
    for word in data.split():
        freq[word] = freq.get(word, 0) + 1

    try:
        most_frequent_word = max(freq, key=freq.get)
        print(f"Most frequent word: {most_frequent_word}")
    except ValueError:
        print("File is empty.")

except FileNotFoundError:
    print("File does not exist.")
