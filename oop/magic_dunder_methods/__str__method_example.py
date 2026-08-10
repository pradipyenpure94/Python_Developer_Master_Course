"""
__str__ method.
Note: This method used for concept-understanding purpose.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, course_name: str) -> None:
        self.name = name
        self.course_name = course_name

    def __str__(self) -> str:
        """Representation of a student object."""
        return (
            f"Name    : {self.name}\n"
            f"Course  : {self.course_name}"
        )


def main() -> None:
    """Run the main program."""
    student_obj = Student(name="Pradip", course_name="Python")
    print("-" * 40)
    print("Student Information:")
    print("-" * 40)
    print(student_obj)
    print("-" * 40)


if __name__ == "__main__":
    main()
