"""
Accept marks of five subjects and calculate total,
percentage and average.
"""

TOTAL_MARKS = 500
TOTAL_SUBJECTS = 5
MIN_MARKS = 0
MAX_MARKS = 100


total_obtained_marks = 0
try:
    for mark in range(1, TOTAL_SUBJECTS + 1):
        marks = int(input(f"Enter marks of subject {mark}: "))
        if not MIN_MARKS <= marks <= MAX_MARKS:
            raise ValueError(
                f"Marks must be between {MIN_MARKS} "
                f"and {MAX_MARKS}."
            )
        total_obtained_marks += marks
    marks_average = total_obtained_marks / TOTAL_SUBJECTS
    percentage = (total_obtained_marks / TOTAL_MARKS) * 100

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Total Marks       : {total_obtained_marks:.2f}")
    print(f"Percentage        : {percentage:.2f}")
    print(f"Average of marks  : {marks_average:.2f}")
