"""Rotate a list left."""

numbers = [1, 2, 3, 4, 5]
left_position = 2

numbers = numbers[left_position:] + numbers[:left_position]
print(numbers)
