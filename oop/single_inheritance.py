"""Single inheritance."""

PF_ACCOUNT_NUMBER_LENGTH = 12


def validate_required_text(field_value: str, field_name: str) -> None:
    """Validate the required text is not empty."""
    if not field_value.strip():
        raise ValueError(f"Employee {field_name} cannot be empty.")


def validate_pf_account_number(pf_account_number: str) -> None:
    """Validate the PF account number."""
    if (
        len(pf_account_number) != PF_ACCOUNT_NUMBER_LENGTH or
        not pf_account_number.isdigit()
    ):
        raise ValueError(
            "Employee PF account number should be "
            f"{PF_ACCOUNT_NUMBER_LENGTH} digits."
        )


class Employee:
    """Represent an employee."""
    company_name = "Accenture"

    def __init__(
        self,
        name: str,
        designation: str,
        pf_account_number: str
    ) -> None:
        validate_required_text(field_value=name, field_name="name")
        validate_required_text(
            field_value=designation,
            field_name="designation"
        )
        validate_pf_account_number(pf_account_number=pf_account_number)
        self.name = name
        self.designation = designation
        self.__pf_account_number = pf_account_number

    def get_pf_account_number(self) -> str:
        """Return the PF account number."""
        return self.__pf_account_number

    def display_employee_information(self) -> None:
        """Display the employee information."""
        print("-" * 40)
        print("Employee Information:")
        print("-" * 40)
        print(f"Company              : {self.company_name}")
        print(f"Name                 : {self.name}")
        print(f"Designation          : {self.designation}")
        print(f"PF Account Number    : {self.get_pf_account_number()}")


class Developer(Employee):
    """Developer derived class."""
    def __init__(
        self,
        name: str,
        designation: str,
        pf_account_number: str,
        language: str
    ) -> None:
        super().__init__(
            name=name,
            designation=designation,
            pf_account_number=pf_account_number
        )
        validate_required_text(
            field_value=language,
            field_name="programming language"
        )
        self.language = language

    def display_developer_information(self) -> None:
        """Display developer information."""
        self.display_employee_information()
        print(f"Programming Language : {self.language}")


def main() -> None:
    """Run the main program."""
    try:
        emp_name = input("Enter the employee name: ").strip()
        emp_designation = input("Enter the employee designation: ").strip()
        pf_account_number = input("Enter the employee PF number: ").strip()
        programming_language = input("Enter the programming language: ").strip()

        developer_obj = Developer(
            name=emp_name,
            designation=emp_designation,
            pf_account_number=pf_account_number,
            language=programming_language
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        developer_obj.display_developer_information()


if __name__ == "__main__":
    main()
