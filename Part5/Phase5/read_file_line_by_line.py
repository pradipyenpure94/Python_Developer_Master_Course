"""Read file line by line."""


from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")
FILE_NAME = FILE_PATH.name


with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    for line in file_obj:
        print(line)

    print(f"{FILE_NAME} read line by line successfully.")
