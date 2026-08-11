"""__delitem__() method."""


class Student:
    """Represent a student."""

    def __init__(self) -> None:
        self.subjects: list[str] = []

    def add_subject(self, subject_name: str) -> None:
        """Add the subject into the subject list."""
        self.subjects.append(subject_name)

    def __getitem__(self, index: int | slice) -> str | list[str]:
        return self.subjects[index]

    def __delitem__(self, index: int | slice) -> None:
        if not isinstance(index, (int, slice)):
            raise TypeError("Index must be an integer or slice.")

        del self.subjects[index]


def main() -> None:
    """Run the main program."""
    student_obj = Student()

    try:
        student_obj.add_subject("DSA")
        student_obj.add_subject("OS")
        student_obj.add_subject("Python")
        student_obj.add_subject("Web Development")
        print(f"Before delete: {student_obj.subjects}")

        del student_obj[1]

    except (TypeError, IndexError) as error:
        print(f"Error: {error}")
    else:
        print(f"After delete: {student_obj.subjects}")


if __name__ == "__main__":
    main()
