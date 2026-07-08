"""Grade calculator."""

MIN_MARKS = 0.00
MAX_MARKS = 100.00

GRADE_A_LIMIT = 90
GRADE_B_LIMIT = 80
GRADE_C_LIMIT = 70
GRADE_D_LIMIT = 60
GRADE_E_LIMIT = 35


def validate_name(name: str) -> None:
    """
    Validate the name.

    Args:
        name (str): Input name.

    Raises:
        ValueError: If not name is empty or contains characters
        other than letters and spaces.
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    if not all(ch.isalpha() or ch.isspace() for ch in name):
        raise ValueError("Name must contain only letters and spaces.")


def validate_marks(marks: float) -> None:
    """
    Validate the marks.

    Args:
        marks (float): Input marks.

    Raises:
        ValueError: If the marks are outside the valid range.
    """
    if not MIN_MARKS <= marks <= MAX_MARKS:
        raise ValueError(
            f"Marks must be between {MIN_MARKS:.2f} and {MAX_MARKS:.2f}.")


def calculate_grade(marks: float) -> str:
    """
    Return a grade.

    Args:
        marks (float): Input marks.

    Returns:
        str: The calculated grade.
    """
    if marks >= GRADE_A_LIMIT:
        return "A"
    if marks >= GRADE_B_LIMIT:
        return "B"
    if marks >= GRADE_C_LIMIT:
        return "C"
    if marks >= GRADE_D_LIMIT:
        return "D"
    if marks >= GRADE_E_LIMIT:
        return "E"
    return "F"


def print_grade_report(name: str, marks: float, grade: str) -> None:
    """
    Print the student grade report.

    Args:
        name (str): Input student name.
        marks (float): Input student marks.
        grade (str): Calculated student grade.
    """
    print("-" * 30)
    print("Grade Report:")
    print("-" * 30)
    print(f"Name  : {name}")
    print(f"Marks : {marks:.2f}")
    print(f"Grade : {grade}")
    print("-" * 30)


def main() -> None:
    """Run the Grade Calculator Application."""
    try:
        # Accept input from user and its validation
        name = input("Enter the name: ").strip()
        validate_name(name=name)

        marks = float(input("Enter the marks: "))
        validate_marks(marks=marks)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # Determine the grade
        grade = calculate_grade(marks=marks)
        # Print grade report
        print_grade_report(name=name, marks=marks, grade=grade)
    finally:
        print("Operation completed.")


if __name__ == "__main__":
    main()
