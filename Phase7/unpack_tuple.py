"""Unpack a tuple and return multiple calculation results."""

# Unpack tuple
numbers = (2, 10, 45)
a, b, c = numbers
print(a)
print(b)
print(c)

# Return multiple calculation results
addition, multiplication = a + b,  a * b * c
print(f"Addition: {addition}")
print(f"Multiplication: {multiplication}")
