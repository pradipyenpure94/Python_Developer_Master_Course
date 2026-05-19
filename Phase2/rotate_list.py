"""Rotate list by left / right."""

numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers)

shift_left = numbers[k:] + numbers[:k]
print(f"Numbers list shift by {k} left position: {shift_left}")
right_shift = numbers[-k:] + numbers[:-k]
print(f"Numbers list shift by {k} right position: {right_shift}")
