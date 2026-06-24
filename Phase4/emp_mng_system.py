"""Employee management system."""

import csv
from pathlib import Path

HEADERS = ["id", "name"]
FILE_PATH = "file_handling/emp_mng_system.csv"


def create_csv_file() -> None:
    """Create an employee management system of CSV file."""
    if not Path(FILE_PATH).exists():
        with open(file=FILE_PATH, mode="w",
                  encoding="utf-8", newline="") as file_obj:
            csv_writer = csv.writer(file_obj)
            csv_writer.writerow(HEADERS)
            file_name = Path(FILE_PATH).name
            print(f"{file_name} is created successfully.")


def load_data() -> list[dict]:
    """Fetch all employee records from CSV file."""
    with open(file=FILE_PATH, mode="r",
              encoding="utf-8") as file_obj:
        csv_reader = csv.DictReader(file_obj)
        return list(csv_reader)


def save_data(employees: list[dict]) -> None:
    """Save employee records into CSV file."""
    with open(file=FILE_PATH, mode="w",
              encoding="utf-8", newline="") as file_obj:
        csv_writer = csv.DictWriter(file_obj, fieldnames=HEADERS)
        csv_writer.writeheader()
        csv_writer.writerows(employees)


def next_employee_id(data: list[dict]) -> int:
    """Auto generate employee IDs."""
    if not data:
        return 1
    return max(int(row['id']) for row in data) + 1


def unique_employee_name(data: list[dict]) -> str | None:
    """Return a unique employee name."""
    emp_name = input("Enter an employee name: ").strip()
    if not emp_name:
        return None

    if " " in emp_name:
        return None

    for row in data:
        if row['name'].casefold() == emp_name.casefold():
            return None

    return emp_name


def add_employee(data: list[dict]) -> None:
    """Add new employee record to the CSV file."""
    # Auto generate next employee Id.
    emp_id = next_employee_id(data)
    emp_name = unique_employee_name(data=data)

    if not emp_name:
        print("Employee name already exists or is invalid.")
        return

    data.append({
        "id": emp_id,
        "name": emp_name
        })

    save_data(data)
    print("New employee record added successfully.")


def search_employee(data: list[dict]) -> None:
    """Search employee record by Employee Id."""
    try:
        emp_id = int(input("Enter an employee Id: "))
        for row in data:
            if row["id"] == str(emp_id):
                print(f"Employee record found: \n"
                      f"Employee Id: {row['id']}\n"
                      f"Employee Name: {row['name']}")
                break
        else:
            print("Employee record not found.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


def update_employee(data: list[dict]) -> None:
    """Update employee record into CSV file."""
    try:
        emp_id = int(input("Enter an employee Id? "))
        emp_name = input("Enter an employee name? ").strip()
        if not emp_name or " " in emp_name:
            print("Employee name cannot be empty or contain spaces.")
            return
        emp_names = set(row.get("name").casefold()
                        for row in data
                        if row.get("id") != str(emp_id) and row.get("name"))
        for row in data:
            if row["id"] == str(emp_id):
                if emp_name.casefold() in emp_names:
                    print("Employee name already exists.")
                    return
                row["name"] = emp_name
                save_data(data)
                print("Employee record updated successfully.")
                break
        else:
            print("Employee record not found.")

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return


def delete_employee(data: list[dict]) -> None:
    """Delete employee record from CSV file."""
    try:
        emp_id = int(input("Enter employee Id to delete? "))
        for row in data:
            if row["id"] == str(emp_id):
                # Delete record from CSV file.
                data.remove(row)
                save_data(data)
                print("Employee record deleted successfully.")
                break
        else:
            print("Employee record not found.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


def main() -> None:
    """Main Program."""
    # Create CSV file if not exist.
    create_csv_file()

    # Load CSV file data.
    data = load_data()

    while True:
        print("Employee Operations:")
        print("1. Add employee")
        print("2. Search employee")
        print("3. Update employee")
        print("4. Delete employee")
        print("5. Exit")

        choice = input("Enter your choice? ")

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please select a valid operations.")
            continue

        elif choice == "5":
            print("Exit from operations.")
            break

        elif choice == "1":
            add_employee(data=data)

        elif choice == "2":
            search_employee(data=data)

        elif choice == "3":
            update_employee(data=data)

        elif choice == "4":
            delete_employee(data=data)


if __name__ == "__main__":
    main()
