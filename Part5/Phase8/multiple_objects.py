"""Create multiple objects from one class."""


class Student:
    """Represent a student."""

    def show_info(self) -> None:
        """Show student information."""
        print("Student class.")


student_obj1 = Student()
student_obj1.show_info()

student_obj2 = Student()
student_obj2.show_info()
