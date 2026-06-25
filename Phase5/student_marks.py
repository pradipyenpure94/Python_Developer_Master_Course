"""
Student Marks Validation.
Marks must be between 0 and 100.
"""

try:
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        raise ValueError("Student marks must be between 0 and 100.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram Interrupted.")
else:
    print(f"Student marks: {marks:.2f}")
finally:
    print("Operation completed.")
