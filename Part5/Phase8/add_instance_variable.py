"""Add instance variable."""


class Student:
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show_info(self) -> None:
        """Show student information."""
        print(f"My name is: {self.name}")


student_obj = Student(name="Pradip")
student_obj.show_info()
