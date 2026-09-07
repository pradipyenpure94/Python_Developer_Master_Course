"""Create an employee data file."""

from pathlib import Path

HEADERS = "id,name\n"

FILE_PATH = Path("Part5/Phase5/employee_data.txt")


def create_txt_file() -> None:
    """Create the employee data file if it does not exist."""
    if not FILE_PATH.exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)


def get_employee_data() -> list[str]:
    """Return the employee data."""
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        next(file_obj)
        return file_obj.readlines()


def save_employee_data(employee: str) -> None:
    """Save employee data to the file."""
    with open(file=FILE_PATH, mode="a", encoding="utf-8") as file_obj:
        file_obj.write(employee)


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
    try:
        emp_id = auto_generate_employee_id()
        emp_name = input("Enter the employee Name: ")
        emp_name = validate_employee_name(name=emp_name)
        emp_data = f"{emp_id},{emp_name}\n"
        save_employee_data(employee=emp_data)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print("Employee added successfully.")


def search_employee_by_id() -> None:
    """Search employee ID."""
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


def main() -> None:
    """Run the main program."""
    # Create File if not exists.
    create_txt_file()

    while True:
        print("1. Add Employee")
        print("2. Search Employee BY ID")
        print("3. Exit")
        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3"}:
                print("Please select a valid option (1-3).")
                continue

            if choice == "3":
                print("Exit from Operations.")
                break

            if choice == "1":
                add_employee()

            if choice == "2":
                search_employee_by_id()

        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
