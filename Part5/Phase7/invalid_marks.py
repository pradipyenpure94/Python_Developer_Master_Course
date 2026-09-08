"""Create custom exception for invalid marks."""


class InvalidMarks(Exception):
    """Custom exception for invalid marks."""


MIN_MARKS = 0
MAX_MARKS = 100

try:
    marks = float(input("Enter the marks: "))
    if not MIN_MARKS <= marks <= MAX_MARKS:
        raise InvalidMarks("Invalid marks input.")
except (ValueError, InvalidMarks) as error:
    print(f"Error: {error}")
else:
    print(f"Marks: {marks}")
