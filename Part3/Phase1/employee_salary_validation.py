"""Employee salary validation using encapsulation."""

MIN_SALARY = 5000


def validate_salary(salary: float) -> None:
    """Validate the employee salary."""
    if salary < MIN_SALARY:
        raise ValueError(
            f"Employee salary must be at least {MIN_SALARY}."
        )


class Employee:
    """Represent an employee."""

    def __init__(self, salary: float) -> None:
        self.salary = salary

    @property
    def salary(self) -> float:
        """Return the employee salary."""
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        validate_salary(salary=salary)
        self.__salary = salary


def main() -> None:
    """Run the main program."""
    try:
        emp_salary = float(input("Enter the employee salary: "))
        employee_object = Employee(salary=emp_salary)
        print(f"Employee Salary: {employee_object.salary}")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
