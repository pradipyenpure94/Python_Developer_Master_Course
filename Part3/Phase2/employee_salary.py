"""
Employee Salary Encapsulation

Make salary private.

Implement:

    - getter
    - setter
    - salary validation

    Rule:
        5000 <= salary <= 150000
"""

MIN_SALARY = 5000
MAX_SALARY = 150000


class Employee:
    """Represent an employee."""

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.set_salary(salary=salary)

    def get_salary(self) -> float:
        """Return the employee salary."""
        return self.__salary

    def set_salary(self, salary: float) -> None:
        """Update and validate the employee salary."""
        if not MIN_SALARY <= salary <= MAX_SALARY:
            raise ValueError(
                "Employee salary must be between "
                f"{MIN_SALARY} and {MAX_SALARY}."
            )
        self.__salary = salary


def main() -> None:
    """Run the main program."""
    try:
        print("-" * 40)
        print("Employee Salary Information:")
        print("-" * 40)
        employee = Employee(name="Pradip", salary=15000)
        print(f"Employee Name           : {employee.name}")
        print(f"Current Salary          : {employee.get_salary():.2f}")

        updated_salary = float(input("Enter the updated employee salary: "))
        employee.set_salary(salary=updated_salary)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Updated Employee Salary : {employee.get_salary():.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()
