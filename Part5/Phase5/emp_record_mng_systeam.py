"""Build a simple file-based record management system."""

from pathlib import Path

HEADER = "id,name\n"

FILE_PATH = Path("Part5/Phase5/emp_record_system.txt")


def create_txt_file() -> None:
    """Create .txt file if does not exist."""
    if not FILE_PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADER)


def save_employees_data(employees: list[str]) -> None:
    """Rewrite the employee data to file."""
    with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
        file_obj.write(HEADER)  # Write Header
        file_obj.writelines(employees)  # Rewrite employee records


def get_employee_data() -> list[str]:
    """Return the employees data."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        next(file_obj)
        return file_obj.readlines()


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


def auto_next_generate_employee_id(employees: list[str]) -> int:
    """Auto generate next available employee ID."""
    if not employees:
        return 1
    return max(int(record.split(",")[0]) for record in employees) + 1


def add_employee(employees: list[str]) -> None:
    """Add a new employee record."""
    try:
        emp_id = auto_next_generate_employee_id(employees=employees)
        emp_name = input("Enter the employee name: ")
        emp_name = validate_employee_name(name=emp_name)
        emp_record = f"{emp_id},{emp_name}\n"
        employees.append(emp_record)
        save_employees_data(employees=employees)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("Added a new employee record successfully.")


def search_employee_by_id(employees: list[str]) -> None:
    """Search an employee by ID."""
    try:
        emp_id = int(input("Enter the employee ID to search employee record:"))

        for record in employees:
            employee_id, employee_name = record.split(",")
            if int(employee_id) == emp_id:
                print("Employee record found.")
                print("Employee Information:")
                print(f"Employee ID    : {employee_id}")
                print(f"Employee Name  : {employee_name}")
                break
        else:
            print("Employee record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


def display_all_employees(employees: list[str]) -> None:
    """Display all employee records."""
    if not employees:
        print("Employee records not found.")
    else:
        print("Employee Information:")
        print("-" * 50)
        print(f"{'ID':>5} | {'Name':<25}")
        print("-" * 50)
        for record in employees:
            employee_id, employee_name = record.split(",")
            print(f"{employee_id:>5} | {employee_name.strip():<25}")
        print("-" * 50)


def update_employee(employees: list[str]) -> None:
    """Update the employee information."""
    try:
        emp_id = int(input("Enter the employee ID to update record: "))

        for index, record in enumerate(employees):
            employee_id, _ = record.split(",")
            if int(employee_id) == emp_id:
                update_name = input("Update the employee name: ")
                update_name = validate_employee_name(name=update_name)
                update_data = f"{employee_id},{update_name}\n"
                employees[index] = update_data
                save_employees_data(employees=employees)
                print("Update the employee records successfully.")
                break
        else:
            print("Employee record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


def delete_employee(employees: list[str]) -> None:
    """Delete the employee record from .txt file."""
    try:
        emp_id = int(input("Enter the employee ID to delete record: "))

        for index, record in enumerate(employees):
            employee_id, _ = record.split(",")
            if int(employee_id) == emp_id:
                employees.pop(index)
                save_employees_data(employees=employees)
                print("Employee record deleted successfully.")
                break
        else:
            print("Employee record not found.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


def main() -> None:
    """Run the main program."""
    # Create .txt file if does not exist.
    create_txt_file()

    employee_records = get_employee_data()

    while True:
        print("Employee Record Management System.")
        print("1. Add Employee")
        print("2. Search Employee By ID")
        print("3. Display All Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3", "4", "5", "6"}:
                print("Please select a valid option (1-6).")
                continue

            if choice == "6":
                print("Exit from Operations.")
                break

            if choice == "1":
                add_employee(employees=employee_records)

            if choice == "2":
                search_employee_by_id(employees=employee_records)

            if choice == "3":
                display_all_employees(employees=employee_records)

            if choice == "4":
                update_employee(employees=employee_records)

            if choice == "5":
                delete_employee(employees=employee_records)

            print("-" * 50)

        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
