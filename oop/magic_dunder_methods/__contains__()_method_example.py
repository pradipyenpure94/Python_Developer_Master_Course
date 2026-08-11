"""__contains__() method."""


class Student:
    """Represent a student."""
    def __init__(self) -> None:
        self.subjects: list[str] = []

    def add_subject(self, subject_name: str) -> None:
        """Add the subject name into the subject list."""
        self.subjects.append(subject_name)

    def __contains__(self, subject_name: str) -> bool:
        if not isinstance(subject_name, str):
            raise TypeError("Subject name must be a string.")

        return subject_name in self.subjects


def main() -> None:
    """Run the main program."""
    student_obj = Student()
    try:
        student_obj.add_subject("DSA")
        student_obj.add_subject("Python")
        student_obj.add_subject("OS")

        print(f"Student subjects: {student_obj.subjects}")
        print(f"DSA exists: {'DSA' in student_obj}")
    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
