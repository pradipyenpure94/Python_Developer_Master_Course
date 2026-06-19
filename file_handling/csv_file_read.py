"""Read entire CSV file."""


import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)

        # Display records with header
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("File does not exist.")
