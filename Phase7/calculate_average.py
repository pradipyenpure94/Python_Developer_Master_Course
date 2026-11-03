"""Calculate the average of five numbers."""

total = 0

for i in range(1, 6):
    number = float(input(f"Enter the number {i}: "))
    total += number

average = total / 5
print(f"Average of 5 numbers: {average:.2f}")
