"""Employee class."""

MIN_EMPLOYEE_SALARY = 5000
MAX_EMPLOYEE_SALARY = 150000
MIN_EMP_ID = 1


class Employee:
    """Employee class representation."""

    def __init__(
        self,
        emp_id: int,
        emp_name: str,
        emp_salary: float,
    ) -> None:

        validate_employee_id(emp_id=emp_id)
        validate_employee_name(emp_name=emp_name)
        validate_employee_salary(emp_salary=emp_salary)

        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def __str__(self) -> str:
        return (
            "Employee Information: \n"
            f"Employee ID: {self.emp_id}\n"
            f"Employee Name: {self.emp_name}\n"
            f"Employee Salary: {self.emp_salary}"
        )


def validate_employee_id(emp_id: int) -> None:
    """Validate the employee ID."""
    if emp_id < MIN_EMP_ID:
        raise ValueError(
            f"Employee ID must be greater than or equal to {MIN_EMP_ID}"
        )


def validate_employee_name(emp_name: str) -> None:
    """Validate the employee name."""
    if not emp_name:
        raise ValueError("Employee name cannot be empty.")
    if not emp_name.replace(" ", "").isalpha():
        raise ValueError(
            "Employee name must contain only alphabetic characters."
        )


def validate_employee_salary(emp_salary: float) -> None:
    """Validate the employee salary."""
    if not MIN_EMPLOYEE_SALARY <= emp_salary <= MAX_EMPLOYEE_SALARY:
        raise ValueError(
            f"Employee salary range must be between {MIN_EMPLOYEE_SALARY} "
            f"and {MAX_EMPLOYEE_SALARY}"
        )


def main() -> None:
    """Run the Main Program."""
    try:
        emp_id = int(input("Enter the employee ID: "))
        emp_name = input("Enter the employee name: ").strip()
        emp_salary = float(input("Enter the employee salary: "))

        emp_obj = Employee(
            emp_id=emp_id,
            emp_name=emp_name,
            emp_salary=emp_salary
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(emp_obj)


if __name__ == "__main__":
    main()
