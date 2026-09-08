"""Create custom exception for invalid salary."""


class InvalidSalary(Exception):
    """Exception for invalid salary."""


MIN_SALARY = 25000
MAX_SALARY = 100000

try:
    salary = float(input("Enter the employee salary: "))
    if not MIN_SALARY <= salary <= MAX_SALARY:
        raise InvalidSalary(
            f"Employee salary must be between {MIN_SALARY} and {MAX_SALARY}."
        )
except (ValueError, InvalidSalary) as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Employee Salary: {salary}")
