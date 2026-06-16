"""Count number of lines."""


try:
    # open file and read all lines.
    with open("file_handling/sample_text.txt", mode="r",
              encoding="utf-8") as file_obj:
        data = file_obj.readlines()
        count_lines = len(data)
        print(f"Count number of lines: {count_lines}")
except FileNotFoundError:
    print("File does not exist.")
