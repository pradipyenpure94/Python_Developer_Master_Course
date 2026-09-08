"""Create an employee data file."""

from pathlib import Path

HEADER = "id,name\n"

FILE_PATH = Path("Part5/Phase5/employee_data.txt")


def create_txt_file() -> None:
    """Create the employee data file if it does not exist."""
    if not FILE_PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADER)


def get_employee_data() -> list[str]:
    """Return all employee records from the data file."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        next(file_obj)
        return file_obj.readlines()


def save_employee_data(employees: list[str]) -> None:
    """Save employee data to the file."""
    with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(HEADER)
        file_obj.writelines(employees)


def validate_employee_name(name: str) -> str:
    """Validate and normalize the employee name."""
    name = name.strip()

    if not name:
        raise ValueError("Employee name cannot be empty.")

    if not all(char.isspace() or char.isalpha() for char in name):
        raise ValueError(
            "Employee name must contain alphabetic letters or spaces."
        )
    return name


def auto_generate_employee_id() -> int:
    """Auto generate next available employee ID."""
    employee_records = get_employee_data()
    if not employee_records:
        return 1

    return max(int(record.split(",")[0]) for record in employee_records) + 1


def add_employee() -> None:
    """Add a new employee record."""
    employee_records = get_employee_data()
    try:
        emp_id = auto_generate_employee_id()
        emp_name = input("Enter the employee Name: ")
        emp_name = validate_employee_name(name=emp_name)
        emp_data = f"{emp_id},{emp_name}\n"
        employee_records.append(emp_data)
        save_employee_data(employees=employee_records)

    except ValueError as error:
        print(f"Error: {error}")
    else:
        print("Employee added successfully.")


def search_employee_by_id() -> None:
    """Search for an employee by ID."""
    employee_records = get_employee_data()
    try:
        emp_id = int(input("Enter employee ID to search: "))
        for record in employee_records:
            # Extract employee ID and name
            employee_id, employee_name = record.split(",")
            if int(employee_id) == emp_id:
                print("Employee record found.")
                print(f"Employee ID   : {employee_id}")
                print(f"Employee Name : {employee_name.strip()}")
                print("-" * 30)
                break
        else:
            print("Employee record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


def update_employee_information() -> None:
    """Update an employee's information."""
    employee_records = get_employee_data()
    try:
        emp_id = int(input("Enter the employee ID: "))
        for index, record in enumerate(employee_records):
            employee_id, _ = record.split(",")
            if int(employee_id) == emp_id:
                update_name = input("Update the employee Name: ")
                update_name = validate_employee_name(name=update_name)
                emp_data = f"{employee_id},{update_name}\n"
                employee_records[index] = emp_data
                save_employee_data(employees=employee_records)
                print("Employee record updated successfully.")
                break
        else:
            print("Employee record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


def main() -> None:
    """Run the main program."""
    # Create File if not exists.
    create_txt_file()

    while True:
        print("1. Add Employee")
        print("2. Search Employee BY ID")
        print("3. Update Employee Information")
        print("4. Exit")
        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3", "4"}:
                print("Please select a valid option (1-4).")
                continue

            if choice == "4":
                print("Exit from Operations.")
                break

            if choice == "1":
                add_employee()

            if choice == "2":
                search_employee_by_id()

            if choice == "3":
                update_employee_information()

        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
