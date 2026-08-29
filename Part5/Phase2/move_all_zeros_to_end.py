"""Move all zeros to the end."""

numbers = [1, 0, 1, 0, 1, 2]
n = len(numbers)

non_zero_pos = 0

for index in range(n):
    if numbers[index] != 0:
        numbers[non_zero_pos], numbers[index] = (
            numbers[index], numbers[non_zero_pos]
        )
        non_zero_pos += 1

print(f"Move all zeros to the end: {numbers}")
