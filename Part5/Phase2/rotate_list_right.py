"""Rotate a list right."""


numbers = [1, 2, 3, 4, 5]
right_position = 2

numbers = numbers[-right_position:] + numbers[:-right_position]
print(f"Rotate list by right: {numbers}")
