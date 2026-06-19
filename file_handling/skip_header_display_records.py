"""Skip header and display records."""


import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)

        # Skip header with display records.
        next(csv_reader)
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("File does not exist.")
