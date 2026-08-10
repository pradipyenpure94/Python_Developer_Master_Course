"""
__repr__() method.
Note: This method is used for concept-understanding purpose.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, course_name: str) -> None:
        self.name = name
        self.course_name = course_name

    def __repr__(self) -> str:
        """The student object __repr__() method."""
        return (
            "Student("
            f"Name={self.name !r}, Course={self.course_name !r}"
            ")"
        )


def main() -> None:
    """Run the main program."""
    student_obj = Student(
        name="Pradip",
        course_name="Python Backend Developer"
    )
    print(repr(student_obj))


if __name__ == "__main__":
    main()
