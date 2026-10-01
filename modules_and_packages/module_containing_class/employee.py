"""Design and develop custom class."""


class Employee:
    """Represent an employee."""
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display(self) -> None:
        print(f"Employee Name  : {self.name}")
        print(f"Employee Email : {self.email}")
