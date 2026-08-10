"""__getitem__() method."""


class Student:
    """Represent a student."""
    def __init__(self) -> None:
        self.subjects: list[str] = []

    def add_subject(self, subject_name: str) -> None:
        """Add subject to the subject list."""
        self.subjects.append(subject_name)

    def __getitem__(self, index: int | slice) -> str | list[str]:
        return self.subjects[index]


def main() -> None:
    """Run the main program."""
    student_obj = Student()
    student_obj.add_subject("DSA")
    student_obj.add_subject("OS")
    student_obj.add_subject("Python")

    print(student_obj[:1])


if __name__ == "__main__":
    main()
