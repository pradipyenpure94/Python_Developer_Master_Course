"""Read CSV using DictReader."""

import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        # Read record using DictReader().
        for row in csv_reader:
            print(row['name'])

except FileNotFoundError:
    print("File does not exist.")
