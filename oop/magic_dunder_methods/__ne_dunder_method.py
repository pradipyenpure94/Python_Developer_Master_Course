"""
__ne__() method.
Note: This method is used for understanding purpose.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, course: str) -> None:
        self.name = name
        self.course = course

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (
            self.name != other.name
            or self.course != other.course
        )


def main() -> None:
    """Run the main program."""
    student_obj1 = Student(name="Pradip", course="Python")
    student_obj2 = Student(name="Amit", course="DSA")
    print(student_obj1 != student_obj2)


if __name__ == "__main__":
    main()
