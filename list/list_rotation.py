"""List rotation by right"""

numbers = [1, 2, 3, 4, 5]
k = 2
right_shift = numbers[-k:] + numbers[:-k]
print(f"Right shift by {k}: {right_shift}")
