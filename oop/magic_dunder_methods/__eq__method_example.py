"""
Example of __eq__() method.
Note: This method is used for concept-understading purpose.
"""


class Student:
    """Represent a student."""
    def __init__(self, name: str, course: str) -> None:
        self.name = name
        self.course = course

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (
            self.course == other.course
            and self.name == other.name
        )


def main() -> None:
    """Run the main program."""
    student_obj1 = Student(name="Pradip", course="Python")
    student_obj2 = Student(name="Pradip", course="DSA")
    print(student_obj1 == student_obj2)


if __name__ == "__main__":
    main()
