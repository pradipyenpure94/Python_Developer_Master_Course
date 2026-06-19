"""Count number of records."""


import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)

        # Count number of records.
        next(csv_reader)
        count = sum(1 for _ in csv_reader)
        print(f"Count number of records: {count}")

except FileNotFoundError:
    print("File does not exist.")
