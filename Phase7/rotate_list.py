"""Rotate a list by K positions."""

numbers = [1, 2, 3, 4, 5]
position = 2

result = numbers[position:] + numbers[:position]
print(result)
