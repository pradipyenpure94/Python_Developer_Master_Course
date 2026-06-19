"""Append new record."""

import csv

with open(file="file_handling/student.csv", mode="a", newline="",
          encoding="utf-8") as file_obj:
    csv_writer = csv.writer(file_obj)

    # Append or add new record into csv file.
    csv_writer.writerows((["id", "name", "age"],
                          [1, "Samiksha", 28],
                          [2, "Sayli", 23]))
