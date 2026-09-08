"""Add instance methods."""


class Student:
    """Represent a student."""

    def __init__(self, name: str, marks: float) -> None:
        self.name = name
        self.marks = marks

    def show_name(self) -> None:
        """Display student name."""
        print(f"Student Name: {self.name}")

    def show_marks(self) -> None:
        """Display student marks."""
        print(f"Student Marks: {self.marks}")


student_obj = Student(name="Pradip", marks=96)
student_obj.show_name()
student_obj.show_marks()
