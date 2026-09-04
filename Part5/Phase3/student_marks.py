"""Create student marks dictionary and calculate result."""

student_marks = {"Marks1": 45, "Marks2": 75, "Marks3": 98}

total_marks = sum(student_marks.values())
percentage = total_marks * 100 / 300
result = "Pass" if percentage >= 35 else "Fail"
print(f"Total Marks : {total_marks}")
print(f"Percentage  : {percentage:.2f}")
print(f"Result      : {result}")
