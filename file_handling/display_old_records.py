"""Display oldest student."""

import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.reader(file_obj)

        # Display oldest student.
        next(csv_reader)
        max_age, name = 0, ""
        for row in csv_reader:
            age = int(row[2])
            if age > max_age:
                max_age = age
                name = row[1]

        # Display oldest student as per age
        print(name, "|", max_age)

except FileNotFoundError:
    print("File does not exist.")
