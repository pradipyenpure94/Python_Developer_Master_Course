"""Sum of all dictionary values."""

students = {"Ajay": 100, "amit": 45}

# Sum of all dictionary values
total = 0

for value in students.values():
    total += value

print(f"Sum of all dictionary values: {total}")
