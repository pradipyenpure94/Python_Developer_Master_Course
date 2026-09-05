"""Lambda to find maximum."""

students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Charlie', 'score': 78}
]

maximum_scores = max(students, key=lambda x: x['score'])
print(f"Maximum Scores: {maximum_scores}")
