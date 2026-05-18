"""Data analysis using set operations."""

python_students = {"Amit", "Ravi", "Neha", "Kiran"}
java_students = {"Neha", "Kiran", "Suresh"}

print(f"All students: {python_students | java_students}")
print(f"Both courses: {python_students & java_students}")
print(f"Only python: {python_students - java_students}")
print(f"Only java: {java_students - python_students}")
