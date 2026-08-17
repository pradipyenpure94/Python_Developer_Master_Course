"""
Student Marks Encapsulation

Make marks private.

Allow marks only between: 0 and 100
"""

MIN_MARKS = 0
MAX_MARKS = 100


class Student:
    """Represent a student."""
    def __init__(self, name: str, marks: float) -> None:
        self.name = name
        self.set_marks(marks=marks)

    def get_marks(self) -> float:
        """Return the student marks."""
        return self.__marks

    def set_marks(self, marks: float) -> None:
        """Validate and update the student marks."""
        if not MIN_MARKS <= marks <= MAX_MARKS:
            raise ValueError(
                f"Student marks must be between {MIN_MARKS} and {MAX_MARKS}."
            )

        self.__marks = marks


def main() -> None:
    """Run the main program."""
    try:
        marks = float(input("Enter the student marks: "))
        student = Student(name="Pradip", marks=marks)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("Student Information: ")
        print(f"Name: {student.name}")
        print(f"Marks: {student.get_marks():.2f}")


if __name__ == "__main__":
    main()
