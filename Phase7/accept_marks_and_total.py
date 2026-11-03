"""Accept three subject marks and calculate total marks."""

total_marks = 0

for i in range(1, 4):
    marks = float(input(f"Enter the subject{i} marks: "))
    total_marks += marks

print(f"Total Marks: {total_marks:.2f}")
