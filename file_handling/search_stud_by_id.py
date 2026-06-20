"""Search Student by ID."""


import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        try:
            # Search student record by student ID.
            student_id = int(input("Enter student ID to search? "))
            for row in csv_reader:
                if int(row['id']) == student_id:
                    print(f"Student Id: {row['id']}\n"
                          f"Name: {row['name']}\n"
                          f"Age: {row['age']}")
                    break
            else:
                print("Student record not found.")

        except ValueError:
            print("Invalid input! Please enter an integer.")

except FileNotFoundError:
    print("File does not exist.")
