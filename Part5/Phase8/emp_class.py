"""Create Employee class with company class variable."""


class Employee:
    """Represent an employee."""
    company_name = "IBM"

    def __init__(self, name: str) -> None:
        self.name = name
