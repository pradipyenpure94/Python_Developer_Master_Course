"""Move all zeros to end."""

numbers = [1, 2, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 1, 4, 5]

if numbers:
    left = 0

    for right, _ in enumerate(numbers):
        if numbers[right] != 0:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1

    print(f"Move all zeros to end: {numbers}")
else:
    print("List is empty!")
