"""Reverse a list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print(f"Reversed List: {numbers}")
