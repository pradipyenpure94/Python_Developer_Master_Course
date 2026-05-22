"""Unpack tuple values."""

numbers = (10, 20, 30, 40, 50)

value1, *value2, value3 = numbers
print(f"Value1: {value1}")
print(f"Value2: {value2}")
print(f"Value3: {value3}")
