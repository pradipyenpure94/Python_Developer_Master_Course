"""Example file Iterator."""

FILE_PATH = "Iterators_and_generators/sample_file.txt"

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    print(next(file_obj))
    print(next(file_obj))
    print(next(file_obj))
    print(next(file_obj))
    print(next(file_obj, "No Value"))
