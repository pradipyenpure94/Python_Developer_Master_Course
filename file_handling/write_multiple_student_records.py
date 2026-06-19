"""Write multiple student records."""

import csv

student_records = ([1, 'Pradip', 32],
                   [2, 'Amit', 28],
                   [3, 'Pranjal', 35],
                   [4, 'Ajay', 34])

with open(file="file_handling/student.csv", mode="w",
          encoding="utf-8") as file_obj:
    csv_writer = csv.writer(file_obj)

    # Add multiple student records into csv file.
    csv_writer.writerow(['id', 'name', 'age'])
    csv_writer.writerows(student_records)
