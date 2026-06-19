"""Create CSV file."""

import csv

with open(file="file_handling/student.csv", mode="w",
          encoding="utf-8") as file_obj:
    csv_writer = csv.writer(file_obj)

    # Add record into csv file.
    csv_writer.writerow(['id', 'name', 'age'])
    csv_writer.writerow([1, 'Pradip', 32])
