"""Find highest salary of employee."""

import csv

highest_salary = 0
emp_name = ""

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        for row in csv_reader:
            try:
                salary = float(row['salary'])
                if salary > highest_salary:
                    highest_salary = salary
                    emp_name = row['name']

            except ValueError:
                print(f"Invalid salary data: Employee Name: {row['name']},"
                      f"Salary: {row['salary']}")

        if emp_name:
            print(f"Highest salary of employee:\n"
                  f"Name: {emp_name}\n"
                  f"Salary: {highest_salary}")
        else:
            print("No employee records found.")

except FileNotFoundError:
    print("File does not exist.")
