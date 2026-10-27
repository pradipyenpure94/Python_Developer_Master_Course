"""Create a grade calculator using if-elif-else."""


def calculate_grade_calculator(marks: float) -> str:
    if marks > 90:
        return "A+ Grade"
    elif marks >= 80:
        return "A Grade"
    elif marks > 60:
        return "B Grade"
    elif marks > 45:
        return "C Grade"
    elif marks >= 35:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    try:
        marks = float(input("Enter the marks: "))
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        result = calculate_grade_calculator(marks=marks)
        print(f"Marks: {marks}, Result: {result}")
