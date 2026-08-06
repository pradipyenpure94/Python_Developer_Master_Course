"""Student Information Management System."""

PASSING_MARK = 35

MIN_STUDENT_ID = 1

MIN_AGE = 18
MAX_AGE = 60

MIN_MARK = 0
MAX_MARK = 100

GRADE_A_PLUS = 90
GRADE_A = 80
GRADE_B = 70
GRADE_C = 60
GRADE_D = 50
TOTAL_SUBJECTS = 3


def validate_student_id(student_id: int) -> None:
    """Validate student ID."""
    if student_id < MIN_STUDENT_ID:
        raise ValueError(
            f"Student ID must be greater than or equal to {MIN_STUDENT_ID}."
            )


def validate_name(name: str) -> None:
    """Validate student name."""
    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError(
            "Student name must contain only alphabetic characters."
        )


def validate_age(age: int) -> None:
    """Validate student age."""
    if not (MIN_AGE <= age <= MAX_AGE):
        raise ValueError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")


def validate_course(course: str) -> None:
    """Validate course name."""
    if not course.strip():
        raise ValueError("Course name cannot be empty.")


def validate_mark(mark: float, subject: str) -> None:
    """Validate subject marks."""
    if not (MIN_MARK <= mark <= MAX_MARK):
        raise ValueError(
            f"{subject} marks must be between "
            f"{MIN_MARK} and {MAX_MARK}."
        )


class Student:
    """Represent a student."""

    def __init__(
        self,
        student_id: int,
        student_name: str,
        age: int,
        course: str,
        python_mark: float,
        sql_mark: float,
        oop_mark: float
    ) -> None:
        validate_student_id(student_id=student_id)
        validate_name(name=student_name)
        validate_age(age=age)
        validate_course(course=course)
        validate_mark(mark=python_mark, subject="Python")
        validate_mark(mark=sql_mark, subject="SQL")
        validate_mark(mark=oop_mark, subject="OOP")

        self.student_id = student_id
        self.student_name = student_name
        self.age = age
        self.course = course
        self.python_mark = python_mark
        self.sql_mark = sql_mark
        self.oop_mark = oop_mark

    def calculate_total(self) -> float:
        """Return total marks."""
        return sum((self.python_mark, self.sql_mark, self.oop_mark))

    def calculate_percentage(self) -> float:
        """Return percentage."""
        return self.calculate_total() / TOTAL_SUBJECTS

    def calculate_result(self) -> str:
        """Return PASS or FAIL."""
        if (
            self.python_mark >= PASSING_MARK and
            self.sql_mark >= PASSING_MARK and
            self.oop_mark >= PASSING_MARK and
            self.calculate_percentage() >= PASSING_MARK
        ):
            return "PASS"
        return "FAIL"

    def calculate_grade(self) -> str:
        """Return grade."""
        percentage = self.calculate_percentage()

        if percentage >= GRADE_A_PLUS:
            return "A+"

        if percentage >= GRADE_A:
            return "A"

        if percentage >= GRADE_B:
            return "B"

        if percentage >= GRADE_C:
            return "C"

        if percentage >= GRADE_D:
            return "D"

        if percentage >= PASSING_MARK:
            return "E"

        return "F"

    def display_student(self) -> None:
        """Display student details."""
        print("\nStudent Information.")
        print("-" * 40)

        print(f"Student ID          : {self.student_id}")
        print(f"Student Name        : {self.student_name}")
        print(f"Age                 : {self.age}")
        print(f"Course              : {self.course}")

        print("\nMarks:")
        print(f"Python              : {self.python_mark:.2f}")
        print(f"SQL                 : {self.sql_mark:.2f}")
        print(f"OOP                 : {self.oop_mark:.2f}")

        print("-" * 40)

        print(f"Total               : {self.calculate_total():.2f}")
        print(f"Percentage          : {self.calculate_percentage():.2f}")
        print(f"Result              : {self.calculate_result()}")
        print(f"Grade               : {self.calculate_grade()}")


def main() -> None:
    """Run the Main Program."""
    try:
        student_id = int(input("Enter the student ID: "))
        student_name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        course = input("Enter the student course: ")
        python_mark = float(input("Enter Python Marks: "))
        sql_mark = float(input("Enter SQL Marks: "))
        oop_mark = float(input("Enter OOP Marks: "))

        student_obj = Student(
            student_id=student_id,
            student_name=student_name,
            age=age,
            course=course,
            python_mark=python_mark,
            sql_mark=sql_mark,
            oop_mark=oop_mark
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        student_obj.display_student()


if __name__ == "__main__":
    main()
