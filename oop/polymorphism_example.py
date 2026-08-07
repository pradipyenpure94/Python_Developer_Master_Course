"""Example of Polymorphism."""


class Person:
    """Person information."""
    def __init__(self, name: str) -> None:
        self.name = name

    def display_information(self) -> None:
        """Display personal information."""
        print("-" * 40)
        print(f"Name: {self.name}")


class Employee(Person):
    """Employee information."""

    def __init__(self, name: str, emp_id: int) -> None:
        super().__init__(name)
        self.emp_id = emp_id

    def display_information(self) -> None:
        """Display employee information."""
        super().display_information()
        print(f"Employee ID: {self.emp_id}")


class Student(Person):
    """Student information."""
    def __init__(self, name: str, roll_no: int) -> None:
        super().__init__(name)
        self.roll_no = roll_no

    def display_information(self) -> None:
        """Display student information."""
        super().display_information()
        print(f"Roll No.: {self.roll_no}")


def main() -> None:
    """Run the Main Program."""
    person_obj = Person(name="Pradip")
    emp_obj = Employee(name="Amit", emp_id=101)
    student_obj = Student(name="Sandeep", roll_no=111)

    for obj in [person_obj, emp_obj, student_obj]:
        obj.display_information()
        print()


if __name__ == "__main__":
    main()
