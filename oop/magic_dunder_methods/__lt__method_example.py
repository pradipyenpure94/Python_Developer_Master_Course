"""__lt__() method."""


class Student:
    """Represent a student."""

    def __init__(self, name: str, marks: float) -> None:
        self.name = name
        self.marks = marks

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks < other.marks


def main() -> None:
    """Run the main program."""
    student_obj1 = Student(name="Pradip", marks=10)
    student_obj2 = Student(name="Amit", marks=50.5)
    print(student_obj1 < student_obj2)


if __name__ == "__main__":
    main()
