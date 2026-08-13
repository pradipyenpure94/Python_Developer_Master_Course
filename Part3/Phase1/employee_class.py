"""Employee -> Manager. Single Inheritance."""
MIN_SALARY = 5000
MAX_SALARY = 50000


def validate_salary(salary: float) -> None:
    """Validate the salary."""
    if not MIN_SALARY <= salary <= MAX_SALARY:
        raise ValueError(
            f"The salary must be between {MIN_SALARY} and {MAX_SALARY}."
        )


class Employee:
    """Represent an employee."""
    def __init__(self, employee_name: str) -> None:
        self.employee_name = employee_name

    def display_employee_information(self) -> None:
        """Display the employee information."""
        print(f"Employee Name: {self.employee_name}")


class Manager(Employee):
    """Represent a manager."""
    def __init__(self, employee_name: str, salary: float) -> None:
        super().__init__(employee_name)
        validate_salary(salary=salary)
        self.salary = salary

    def display_manager_information(self) -> None:
        """Display the manager information."""
        print(f"Manager Salary: {self.salary}")


def main() -> None:
    """Run the main program."""
    try:
        manager_object = Manager(employee_name="Pradip", salary=30000)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        manager_object.display_employee_information()
        manager_object.display_manager_information()


if __name__ == "__main__":
    main()
