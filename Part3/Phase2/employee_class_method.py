"""
Employee Class Method

Create an Employee class with a class variable:

    company_name

Create a class method to change the company name.
"""


class Employee:
    """Represent an employee."""

    company_name = "ABC Technology."

    @classmethod
    def change_company_name(cls, new_company_name: str) -> None:
        """Change the company name."""
        cls.company_name = new_company_name


def main() -> None:
    """Run the main program."""
    print(f"Old Company Name: {Employee.company_name}")
    Employee.change_company_name("XYZ Technology")
    print(f"New company Name: {Employee.company_name}")


if __name__ == "__main__":
    main()
