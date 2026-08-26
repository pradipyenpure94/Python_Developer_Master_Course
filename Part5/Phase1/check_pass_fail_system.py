"""Create a simple pass/fail system."""

MAX_MARKS = 100
MIN_MARKS = 0
PASS_MARKS = 35


try:
    marks = int(input("Enter the marks: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if PASS_MARKS <= marks <= MAX_MARKS:
        print("Pass.")
    elif marks < MIN_MARKS or marks > MAX_MARKS:
        print(
            f"Invalid input. Marks must be between {MIN_MARKS} "
            f"and {MAX_MARKS}."
        )
    else:
        print("Fail.")
