"""Calculate percentage from user-entered marks."""

total_marks = 0
count = 0

for i in range(1, 4):
    count += 1
    marks = float(input(f"Enter the subject{i} marks: "))
    total_marks += marks

marks_percentage = total_marks * 100 / 100 * 3
print(f"Marks (%): {marks_percentage:.2f}")
