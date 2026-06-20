"""Filter employee with Salary > 50000."""

import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        for row in csv_reader:
            try:
                salary = float(row['salary'])
                if salary > 50000:
                    print(f"{row['name']}, {salary}")

            except ValueError:
                print(f"Invalid salary data: {row['name']}, {row['salary']}")

except FileNotFoundError:
    print("File does not exist.")
