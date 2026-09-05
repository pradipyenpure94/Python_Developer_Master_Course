"""Lambda to find minimum."""

students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Charlie', 'score': 78}
]

minimum_scores = min(students, key=lambda student: student['score'])
print(f"Minimum score: {minimum_scores}")
