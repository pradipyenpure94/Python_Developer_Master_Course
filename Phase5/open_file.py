"""
Open a File.
Handle FileNotFoundError
"""

import csv

try:
    with open("file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("File does not exist.")
except PermissionError:
    print("Permission denied.")
else:
    print("File read successfully.")
finally:
    print("Operation completed.")
