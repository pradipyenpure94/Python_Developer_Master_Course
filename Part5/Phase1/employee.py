"""
Accept employee name, ID and salary and display formatted employee
information.
"""

MIN_SALARY = 20000
MAX_SALARY = 100000


def validate_employee_salary(salary: float) -> None:
    """Validate the employee salary."""
    if not MIN_SALARY <= salary <= MAX_SALARY:
        raise ValueError(
            f"Employee Salary must be between {MIN_SALARY} "
            f"and {MAX_SALARY}."
        )


def validate_employee_name(name: str) -> str:
    """Validate and normalize the employee name."""
    name = " ".join(name.split())
    if not name:
        raise ValueError("Employee name cannot be empty.")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only characters and spaces.")
    return name


def validate_employee_id(emp_id: str) -> str:
    """Validate the employee ID."""
    if not emp_id:
        raise ValueError("Employee ID cannot be empty.")
    if not emp_id.isdigit():
        raise ValueError("Employee ID must contain only digits.")
    return emp_id


try:
    name = input("Enter the employee name: ").strip()
    name = validate_employee_name(name=name)
    emp_id = input("Enter the employee ID: ").strip()
    emp_id = validate_employee_id(emp_id=emp_id)
    salary = float(input("Enter the employee salary: "))
    validate_employee_salary(salary=salary)

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print("-" * 50)
    print("Employee Information:")
    print("-" * 50)
    print(f"Name     : {name}")
    print(f"ID       : {emp_id}")
    print(f"Salary   : {salary:.2f}")
    print("-" * 50)
