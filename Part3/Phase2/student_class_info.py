"""
__str__()

Create a Student class and implement __str__() so that:

print(student)

displays meaningful student information.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, grade: str, course: str) -> None:
        self.name = name
        self.grade = grade
        self.course = course

    def __str__(self) -> str:
        """Return the formatted student information."""
        return (
            f"Name    : {self.name}\n"
            f"Course  : {self.course}\n"
            f"Grade   : {self.grade}"
        )


def main() -> None:
    """Run the main program."""
    student = Student(name="Pradip", course="Python", grade="A")
    print(student)


if __name__ == "__main__":
    main()
