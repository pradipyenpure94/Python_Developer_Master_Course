"""Create dictionary from two lists."""

student_names = ["ajay", "amit"]
student_marks = [100, 75]

# Create dictionary from two lists using zip()
students = dict(zip(student_names, student_marks))
print(f"Students: {students}")
