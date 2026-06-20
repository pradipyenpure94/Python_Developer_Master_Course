"""Write CSV using DictWriter."""

import csv

with open(file="file_handling/write_csv_file.csv", mode="w",
          encoding="utf-8") as file_obj:
    field_names = ["id", "name", "age"]
    csv_writer = csv.DictWriter(file_obj, fieldnames=field_names)

    # Write CSV file header
    csv_writer.writeheader()

    # Add new record into the CSV file.
    csv_writer.writerow({'id': 1,
                         'name': 'Pradip',
                         'age': 32})
