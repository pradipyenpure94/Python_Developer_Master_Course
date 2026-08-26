"""Student Grading system."""



MIN_MARKS = 0
MAX_MARKS = 100

GRADE_A = 90
GRADE_B = 80
GRADE_C = 50
GRADE_D = 35


try:
    marks = int(input("Enter the marks: "))
    if not MIN_MARKS <= marks <= MAX_MARKS:
        raise ValueError(
            "Invalid input. "
            f"Marks must be between {MIN_MARKS} and {MAX_MARKS}."
        )
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if marks >= GRADE_A:
        print("Grade A")
    elif marks >= GRADE_B:
        print("Grade B")
    elif marks >= GRADE_C:
        print("Grade C")
    elif marks >= GRADE_D:
        print("Pass")
    else:
        print("Fail")
