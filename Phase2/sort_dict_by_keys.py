"""Sort dictionary by keys."""

student_marks = {"ajay": 100, "pradip": 96, "deepak": 45, "chitan": 75}

sorted_by_key = dict(sorted(student_marks.items(), key=lambda item: item[0]))
print(f"Sorted dictionary by key: {sorted_by_key}")
