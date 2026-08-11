"""__iter__() method."""


class Student:
    """Represent a student."""
    def __init__(self):
        self.subjects: list[str] = []

    def add_subject(self, subject_name: str) -> None:
        """Add the subject name into the subjects list."""
        self.subjects.append(subject_name)

    def __iter__(self):
        return iter(self.subjects)


def main() -> None:
    """Run the main program."""
    student_obj = Student()

    student_obj.add_subject("DSA")
    student_obj.add_subject("Python")
    student_obj.add_subject("OS")
    student_obj.add_subject("Web")

    for subject in student_obj:
        print(f"- {subject}")


if __name__ == "__main__":
    main()
