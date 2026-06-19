"""Display only names."""


import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)

        # Display names only.
        next(csv_reader)
        for _, name, _ in csv_reader:
            print(name)

except FileNotFoundError:
    print("File does not exist.")
