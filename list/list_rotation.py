"""List rotation by left"""

numbers = [1, 2, 3, 4, 5]

k = 2
left_shift = numbers[k:] + numbers[:k]
print(f"Left shift by {k}: {left_shift}")
