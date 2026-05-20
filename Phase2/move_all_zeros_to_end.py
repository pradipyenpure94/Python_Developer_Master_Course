"""Move all zeros to end."""

numbers = [1, 2, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 1, 4, 5]

if numbers:
    numbers.sort(key=lambda x: x == 0)
    print(f"Move all zeros to end: {numbers}")
else:
    print("List is empty!")
