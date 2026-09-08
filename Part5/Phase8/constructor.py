"""Implement a contructor using __init__()."""


class Student:
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        """Student show name."""
        print(f"Student Name: {self.name}")


student_obj = Student(name="Pradip")
student_obj.show_name()
