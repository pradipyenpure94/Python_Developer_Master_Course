"""Find student with higest marks."""

student_marks = {"Pradip": 96, "Amit": 98, "Ajay": 100, "Akshay": 85,
                 "Sanjay": 100}

highest_marks = max(student_marks.values())
top_students = {k: v
                for k, v in student_marks.items()
                if v == highest_marks
                }
print(f"Top students: {top_students}")
