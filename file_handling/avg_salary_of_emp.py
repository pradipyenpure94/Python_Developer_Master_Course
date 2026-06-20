"""Calculate average salary of employee."""

import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        # Calculate average salary of employees.
        count = 0
        total_salary = 0
        for row in csv_reader:
            try:
                total_salary += float(row['salary'])
                count += 1
            except ValueError:
                print(f"Invalid salary data: {row}")

        if count > 0:
            avg_salary = total_salary / count
            print(f"Average salary of employees: {avg_salary:.2f}")
        else:
            print("No employee records found.")

except FileNotFoundError:
    print("File does not exist.")
