"""Employee -> Python Developer (Ex. of Inheritance)."""


MIN_EMPLOYEE_ID = 1


def validate_employee_id(employee_id: int) -> None:
    """Validate the employee ID."""
    if employee_id < MIN_EMPLOYEE_ID:
        raise ValueError(
            f"Employee ID must be greater than or equal to {MIN_EMPLOYEE_ID}"
        )


def validate_name(name: str, field_name: str) -> None:
    """
    Validate that the input contains only alphabetic
    characters and spaces.
    """
    if not name.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    if not all(
        char.isalpha() or char.isspace()
        for char in name
    ):
        raise ValueError(
            f"{field_name} must contain only alphabetic characters.")


class Employee:
    """Represent an employee"""
    def __init__(self, employee_id: int, employee_name: str) -> None:
        validate_employee_id(employee_id=employee_id)
        validate_name(name=employee_name, field_name="Employee name")

        self.employee_id = employee_id
        self.employee_name = employee_name

    def display_employee(self) -> None:
        """Display employee details."""
        print(f"Employee ID             : {self.employee_id}")
        print(f"Employee Name           : {self.employee_name}")


class PythonDeveloper(Employee):
    """Represent a Python developer."""
    def __init__(
        self,
        employee_id: int,
        employee_name: str,
        programming_language: str
    ) -> None:
        super().__init__(employee_id, employee_name)
        validate_name(
            name=programming_language,
            field_name="Programming Language"
        )

        self.programming_language = programming_language

    def display_developer(self) -> None:
        """Display developer details."""
        self.display_employee()
        print(f"Programming Language    : {self.programming_language}")


def main() -> None:
    """Run the Main Program."""
    try:
        employee_id = int(input("Enter the employee ID: "))
        employee_name = input("Enter the employee name: ")
        programming_language = input("Enter the Programming Language: ")

        developer = PythonDeveloper(
            employee_id=employee_id,
            employee_name=employee_name,
            programming_language=programming_language
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        developer.display_developer()


if __name__ == "__main__":
    main()
