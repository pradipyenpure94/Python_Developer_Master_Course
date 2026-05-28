"""Sort dictionary by values."""

student_marks = {"deepak": 45, "Ajay": 63, "Pradip": 100, "chintan": 75}

sorted_by_value = dict(sorted(student_marks.items(), key=lambda item: item[1]))
print(f"Sorted dictionary by values: {sorted_by_value}")
