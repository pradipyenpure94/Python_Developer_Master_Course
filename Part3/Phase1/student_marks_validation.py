"""Student marks validation using encapsulation."""

MIN_MARKS = 0
MAX_MARKS = 100


def validate_student_marks(marks: float) -> None:
    """Validate the student marks."""
    if not MIN_MARKS <= marks <= MAX_MARKS:
        raise ValueError("The marks should be between 0 and 100.")


class Student:
    """Represent a student."""
    def __init__(self, marks: float) -> None:
        self.marks = marks

    @property
    def marks(self) -> float:
        """Return the student marks."""
        return self.__marks

    @marks.setter
    def marks(self, marks: float) -> None:
        """Validate and set the student marks."""
        validate_student_marks(marks=marks)
        self.__marks = marks


def main() -> None:
    """Run the main program."""
    try:
        marks = float(input("Enter the student marks: "))
        student_obj = Student(marks=marks)
        print(f"Student marks: {student_obj.marks}")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
