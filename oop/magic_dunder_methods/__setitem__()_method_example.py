"""__setitem__() method."""


class Student:
    """Represent a student."""

    def __init__(self) -> None:
        self.subjects: list[str] = []

    def add_subject(self, subject: str) -> None:
        """Add the subject to the subject list."""
        self.subjects.append(subject)

    def __getitem__(self, index: int | slice) -> str | list[str]:
        """Return a subject or subjects."""
        return self.subjects[index]

    def __setitem__(
        self,
        index: int | slice,
        subject_name: str | list[str],
    ) -> None:
        """Set one or multiple subjects."""

        if isinstance(index, int):
            if not isinstance(subject_name, str):
                raise TypeError("Subject name must be a string.")
            if not subject_name.strip():
                raise ValueError("Subject name cannot be empty.")

        elif isinstance(index, slice):
            if not isinstance(subject_name, list):
                raise TypeError("Subject names must be a list.")
            if not all(
                isinstance(subject, str)
                for subject in subject_name
            ):
                raise TypeError("All subject names must be strings.")
            if any(not subject.strip() for subject in subject_name):
                raise ValueError("Subject names cannot be empty.")
        else:
            raise TypeError("Index must be integer or slice.")

        self.subjects[index] = subject_name


def main() -> None:
    """Run the main program."""

    try:
        student_obj = Student()
        student_obj.add_subject(subject="OS")
        student_obj.add_subject(subject="DSA")
        student_obj.add_subject(subject="Python")
        student_obj.add_subject(subject="Web Development")
        print(f"Before update: {student_obj.subjects}")
        student_obj[3] = "Django"

    except (TypeError, ValueError, IndexError) as error:
        print(f"Error: {error}")
    else:
        print(f"After update: {student_obj.subjects}")


if __name__ == "__main__":
    main()
