"""
Student Result

Create a Student class with marks for 5 subjects.

Calculate:

    total
    percentage
    grade
"""

GRADE_A = 80
GRADE_B = 70
PASS = 35
TOTAL_MAX_MARKS = 500


class Student:
    """Represent a student."""
    def __init__(
        self,
        mark1: float,
        mark2: float,
        mark3: float,
        mark4: float,
        mark5: float
    ) -> None:
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5

    def get_total_marks(self) -> float:
        """Return the total marks of student."""
        return self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5

    def get_percentage(self) -> float:
        """Return the percentage of student."""
        return (self.get_total_marks() / TOTAL_MAX_MARKS) * 100

    def get_grade(self) -> str:
        """Return the grade of student."""
        student_percentage = self.get_percentage()

        if student_percentage >= GRADE_A:
            return "Grade A"
        elif student_percentage >= GRADE_B:
            return "Grade B"
        elif student_percentage >= PASS:
            return "Pass"
        return "Fail"


def main() -> None:
    """Run the main program."""
    student = Student(mark1=96, mark2=45, mark3=45, mark4=20, mark5=78)
    print("-" * 40)
    print("Student Information:")
    print("-" * 40)
    print(f"Total Marks   : {student.get_total_marks():.2f}")
    print(f"Percentage    : {student.get_percentage():.2f}%")
    print(f"Grade         : {student.get_grade()}")
    print("-" * 40)


if __name__ == "__main__":
    main()
