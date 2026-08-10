"""__len__() method."""


class Student:
    """Represent a student."""
    def __init__(self) -> None:
        self.subjects: list[str] = []

    def add_subject(self, subject_name: str) -> None:
        """Add the subject to the subjects list."""
        self.subjects.append(subject_name)

    def __len__(self) -> int:
        """Return the number of subjects into the subject list."""
        return len(self.subjects)


def main() -> None:
    """Run the main program."""
    student_obj = Student()
    student_obj.add_subject(subject_name="DSA")
    student_obj.add_subject(subject_name="Python")
    student_obj.add_subject(subject_name="OS")
    student_obj.add_subject(subject_name="Web Development")
    print(f"Number of subject: {len(student_obj)}")


if __name__ == "__main__":
    main()
