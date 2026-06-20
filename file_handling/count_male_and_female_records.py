"""Count Male and Female Employees."""

import csv

try:
    with open(file="file_handling/read_csv_file.csv", mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)

        # Count of male and female employees
        count_male_emp = 0
        count_female_emp = 0
        for row in csv_reader:
            if row["gender"] == "M":
                count_male_emp += 1
            elif row['gender'] == "F":
                count_female_emp += 1

        print(f"Count of male employee: {count_male_emp}")
        print(f"Count of female employee: {count_female_emp}")

except FileNotFoundError:
    print("File does not exist.")
